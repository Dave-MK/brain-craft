"""python test_cases.py -- checks the EXPLAIN ANALYZE lab (SQLite's EXPLAIN QUERY PLAN)."""

import os
import sqlite3
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def load_sql(conn, filename):
    with open(os.path.join(HERE, filename), encoding="utf-8") as f:
        conn.executescript(f.read())


def query_plan_text(conn, sql):
    rows = conn.execute(f"EXPLAIN QUERY PLAN {sql}").fetchall()
    return " ".join(row[-1] for row in rows)


def main():
    conn = sqlite3.connect(":memory:")
    load_sql(conn, "fixture.sql")

    query = "SELECT * FROM readings WHERE source_id = 'substation-12'"

    plan_before = query_plan_text(conn, query)
    if "SEARCH" in plan_before:
        print("FAIL: the query is already using an index before you've added one -- check your fixture.")
        return 1

    starter_path = os.path.join(HERE, "starter.sql")
    with open(starter_path, encoding="utf-8") as f:
        starter_sql = f.read()

    try:
        conn.executescript(starter_sql)
    except sqlite3.Error as e:
        print(f"FAIL: starter.sql raised an error: {e}")
        return 1

    plan_after = query_plan_text(conn, query)
    if "SEARCH" not in plan_after:
        print(f"FAIL: after your CREATE INDEX, the query plan still shows a scan, not a search: '{plan_after}'")
        return 1

    print(f"PASS: query plan changed from a full scan to an index search: '{plan_after}'")
    return 0


if __name__ == "__main__":
    sys.exit(main())
