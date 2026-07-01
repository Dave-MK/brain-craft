"""python test_cases.py -- checks the Resolve and Verify lab."""

import os
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

    if os.path.exists(os.path.join(repo_dir, ".git", "MERGE_HEAD")):
        fail("a merge is still in progress (MERGE_HEAD exists) -- finish resolving and commit it.")

    status_lines = run_git(["status", "--porcelain"], repo_dir).stdout.strip().splitlines()
    unmerged = [line for line in status_lines if "U" in line[:2]]
    if unmerged:
        fail(f"unresolved/unmerged paths remain: {unmerged}")

    file_path = os.path.join(repo_dir, "digital_twin", "classification.py")
    with open(file_path) as f:
        content = f.read()

    for marker in ("<<<<<<<", "=======", ">>>>>>>"):
        if marker in content:
            fail(f"leftover conflict marker '{marker}' found in classification.py -- the conflict isn't fully resolved.")

    try:
        compile(content, file_path, "exec")
    except SyntaxError as e:
        fail(f"digital_twin/classification.py is not valid Python after your resolution: {e}")

    branches_raw = run_git(["branch", "--list"], repo_dir).stdout
    branch_names = [b.strip().lstrip("* ") for b in branches_raw.strip().splitlines() if b.strip()]
    main_name = "main" if "main" in branch_names else ("master" if "master" in branch_names else None)

    is_ancestor = run_git(["merge-base", "--is-ancestor", "branch-b", main_name], repo_dir)
    if is_ancestor.returncode != 0:
        fail("branch-b has not actually been merged into your main branch yet.")

    print("PASS: conflict resolved cleanly, no leftover markers, file is valid Python, branch-b is merged.")


if __name__ == "__main__":
    main()
