"""python test_cases.py -- checks the Pull Request Workflow lab."""

import os
import re
import subprocess
import sys


def find_repo_dir():
    if os.path.isdir(".git"):
        return "."
    starter = os.path.join(os.path.dirname(os.path.abspath(__file__)), "starter")
    if os.path.isdir(os.path.join(starter, ".git")):
        return starter
    return None


def run_git(args, cwd):
    return subprocess.run(["git", *args], capture_output=True, text=True, cwd=cwd)


def fail(message):
    print(f"FAIL: {message}")
    sys.exit(1)


def main():
    repo_dir = find_repo_dir()
    if repo_dir is None:
        fail("no repo found -- did you run `python setup_repo.py`?")

    remotes = run_git(["remote"], repo_dir).stdout.strip().splitlines()
    if "origin" not in remotes:
        fail("no 'origin' remote configured -- did you run `python setup_repo.py`?")

    branches_raw = run_git(["branch", "--list"], repo_dir).stdout
    branch_names = [b.strip().lstrip("* ") for b in branches_raw.strip().splitlines() if b.strip()]
    main_name = "main" if "main" in branch_names else ("master" if "master" in branch_names else None)
    feature_branches = [b for b in branch_names if b != main_name]
    if not feature_branches:
        fail("no feature branch found -- create one for your change.")
    feature_branch = feature_branches[0]

    only_on_branch = run_git(["log", f"{main_name}..{feature_branch}", "--oneline"], repo_dir).stdout.strip()
    if not only_on_branch:
        fail(f"'{feature_branch}' has no commits of its own -- make and commit a real change.")

    remote_check = run_git(["rev-parse", f"origin/{feature_branch}"], repo_dir)
    if remote_check.returncode != 0:
        fail(f"'{feature_branch}' has not been pushed to origin yet (git push -u origin {feature_branch}).")

    pr_path = os.path.join(repo_dir, "PULL_REQUEST.md")
    if not os.path.isfile(pr_path):
        fail("PULL_REQUEST.md not found -- write a pull-request description in this folder.")
    with open(pr_path) as f:
        pr_text = f.read()
    if len(pr_text.strip()) < 80:
        fail("PULL_REQUEST.md is too short to actually explain what changed and why.")

    checklist_items = re.findall(r"^\s*[-*]\s+.+", pr_text, re.MULTILINE)
    if len(checklist_items) < 2:
        fail("PULL_REQUEST.md should include a reviewer checklist with at least two specific items (as a markdown list).")

    print(f"PASS: '{feature_branch}' pushed to origin, PULL_REQUEST.md present with a {len(checklist_items)}-item checklist.")


if __name__ == "__main__":
    main()
