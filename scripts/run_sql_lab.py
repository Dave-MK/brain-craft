"""Run a SQL lab's tests against an in-memory SQLite database.

Usage:
    python scripts/run_sql_lab.py labs/03-sql/<lab-name>

Convention each lab directory follows:
    fixture.sql      (optional) schema + seed data, loaded first
    starter.sql       the learner's answer -- typically CREATE VIEW statements
                      for pure-SELECT exercises, or CREATE TABLE for schema labs
    test_cases.sql    exactly ONE SELECT statement (built from UNION ALL'd
                      sub-selects) that returns zero rows if every check
                      passes, or one human-readable failure_reason row per
                      failed check

SQLite stands in for the "real" database engine (still an open question
in docs/12-database/overview.md) purely so labs are runnable without any
installed service. A handful of Postgres-specific lesson examples (SERIAL,
EXPLAIN ANALYZE timing) don't translate 1:1 -- where that matters, the
lab's own README says so explicitly rather than silently pretending it's
identical.
"""

import sqlite3
import sys
from pathlib import Path


def run_lab(lab_dir):
    lab_dir = Path(lab_dir)
    conn = sqlite3.connect(":memory:")
    conn.execute("PRAGMA foreign_keys = ON;")
    cur = conn.cursor()

    fixture_path = lab_dir / "fixture.sql"
    if fixture_path.exists():
        cur.executescript(fixture_path.read_text(encoding="utf-8"))

    starter_path = lab_dir / "starter.sql"
    if not starter_path.exists():
        print(f"FAIL: no starter.sql found in {lab_dir}")
        return 1
    try:
        cur.executescript(starter_path.read_text(encoding="utf-8"))
    except sqlite3.Error as e:
        print(f"FAIL: starter.sql raised an error: {e}")
        return 1

    test_path = lab_dir / "test_cases.sql"
    if not test_path.exists():
        print(f"FAIL: no test_cases.sql found in {lab_dir}")
        return 1

    try:
        cur.execute(test_path.read_text(encoding="utf-8"))
        failures = cur.fetchall()
    except sqlite3.Error as e:
        print(f"FAIL: test_cases.sql raised an error (often means starter.sql didn't create the expected view/table): {e}")
        return 1

    if failures:
        print(f"FAIL: {len(failures)} check(s) failed:")
        for row in failures:
            print(f"  - {row[0]}")
        return 1

    print("PASS: all checks passed.")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python run_sql_lab.py <lab_dir>")
        sys.exit(2)
    sys.exit(run_lab(sys.argv[1]))
