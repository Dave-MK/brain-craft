"""Generate docs/08-knowledge-graph/knowledge-graph.json from lessons/**/*.lesson.json.

The knowledge graph is never hand-authored separately from lesson content —
that would let the two drift apart, exactly the "curriculum rot" the Living
Curriculum system (docs/09-content-engine/overview.md) exists to prevent.
Every node here is derived directly from a lesson file's own fields.

Run from the repo root:
    python scripts/generate_knowledge_graph.py

Exits non-zero if any lesson fails schema validation, any node references
a missing prerequisite, or the prerequisite graph contains a cycle.
"""

import glob
import json
import sys
from pathlib import Path

import jsonschema

REPO_ROOT = Path(__file__).resolve().parent.parent
LESSON_SCHEMA_PATH = REPO_ROOT / "schemas" / "lesson.schema.json"
NODE_SCHEMA_PATH = REPO_ROOT / "schemas" / "concept-node.schema.json"
OUTPUT_PATH = REPO_ROOT / "docs" / "08-knowledge-graph" / "knowledge-graph.json"

# Mastery policy: uniform baseline, tightened for boss battles. Documented
# here rather than per-lesson because it's a curriculum-wide policy decision
# (docs/01-learning-science/overview.md: mastery learning, not time-in-lesson),
# not something each lesson author should re-decide independently.
BASE_MASTERY_THRESHOLD = {
    "minAssessmentScore": 0.8,
    "requiresTeachBack": True,
    "requiresLabPass": True,
}
BOSS_BATTLE_MIN_SCORE = 0.9


def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def build_node(lesson):
    threshold = dict(BASE_MASTERY_THRESHOLD)
    if lesson.get("isBossBattle"):
        threshold["minAssessmentScore"] = BOSS_BATTLE_MIN_SCORE

    return {
        "id": lesson["knowledgeGraphNodeId"],
        "title": lesson["concept"],
        "skillFolder": lesson["skillFolder"],
        "missionId": lesson["missionId"],
        "prerequisites": sorted(lesson["dependencies"]),
        "masteryThreshold": threshold,
        "lessonId": lesson["id"],
        "isBossBattle": lesson.get("isBossBattle", False),
        "capstoneContribution": lesson["capstoneContribution"],
    }


def detect_cycle(nodes_by_id):
    visited, stack = set(), set()

    def dfs(node_id):
        if node_id in stack:
            return [node_id]
        if node_id in visited:
            return None
        visited.add(node_id)
        stack.add(node_id)
        for dep in nodes_by_id[node_id]["prerequisites"]:
            if dep in nodes_by_id:
                cycle = dfs(dep)
                if cycle:
                    return cycle + [node_id]
        stack.discard(node_id)
        return None

    for node_id in nodes_by_id:
        cycle = dfs(node_id)
        if cycle:
            return cycle
    return None


def main():
    lesson_schema = load_json(LESSON_SCHEMA_PATH)
    node_schema = load_json(NODE_SCHEMA_PATH)
    lesson_validator = jsonschema.Draft202012Validator(lesson_schema)
    node_validator = jsonschema.Draft202012Validator(node_schema)

    lesson_paths = sorted(glob.glob(str(REPO_ROOT / "lessons" / "*" / "*.lesson.json")))
    if not lesson_paths:
        print("No lesson files found — is scripts/ being run from the repo root?", file=sys.stderr)
        return 1

    nodes = []
    errors = []

    for path in lesson_paths:
        lesson = load_json(path)
        lesson_errors = list(lesson_validator.iter_errors(lesson))
        if lesson_errors:
            for e in lesson_errors:
                errors.append(f"{path}: {list(e.path)}: {e.message}")
            continue

        node = build_node(lesson)
        node_errors = list(node_validator.iter_errors(node))
        for e in node_errors:
            errors.append(f"{path} (derived node): {list(e.path)}: {e.message}")
        nodes.append(node)

    nodes_by_id = {n["id"]: n for n in nodes}

    missing_edges = []
    for node in nodes:
        for dep in node["prerequisites"]:
            if dep not in nodes_by_id:
                missing_edges.append(f"{node['id']} -> {dep}")

    cycle = detect_cycle(nodes_by_id) if not missing_edges else None

    if errors or missing_edges or cycle:
        print("Knowledge graph generation FAILED:", file=sys.stderr)
        for e in errors:
            print(f"  schema error: {e}", file=sys.stderr)
        for m in missing_edges:
            print(f"  missing prerequisite edge: {m}", file=sys.stderr)
        if cycle:
            print(f"  cycle detected: {' -> '.join(cycle)}", file=sys.stderr)
        return 1

    edge_count = sum(len(n["prerequisites"]) for n in nodes)
    by_mission = {}
    for n in nodes:
        by_mission.setdefault(n["missionId"], 0)
        by_mission[n["missionId"]] += 1

    output = {
        "generatedFrom": "lessons/**/*.lesson.json",
        "generatedOn": "2026-07-01",
        "nodeCount": len(nodes),
        "edgeCount": edge_count,
        "nodesByMission": by_mission,
        "validation": {
            "allLessonsSchemaValid": True,
            "missingPrerequisiteEdges": [],
            "cycleDetected": False,
        },
        "nodes": sorted(nodes, key=lambda n: n["id"]),
    }

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"Wrote {len(nodes)} nodes, {edge_count} edges to {OUTPUT_PATH.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
