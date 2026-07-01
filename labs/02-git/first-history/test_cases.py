"""Check test_cases.py for the First History lab.

Run with:
    python test_cases.py

Works whether you run it from this folder (it looks for your repo in
./starter) or from inside your repo itself (it checks the current
directory first).
"""

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


GENERIC_MESSAGES = {"update", "fix", "commit", "wip", "changes", "initial commit", "test"}


def run_git(args, cwd):
    return subprocess.run(["git", *args], capture_output=True, text=True, cwd=cwd)


def fail(message):
    print(f"FAIL: {message}")
    sys.exit(1)


def main():
    repo_dir = find_repo_dir()
    if repo_dir is None:
        fail("no .git directory found in the current folder or ./starter -- did you run `git init`?")

    log = run_git(["log", "--oneline"], repo_dir)
    if log.returncode != 0:
        fail("`git log` failed -- have you made at least one commit?")
    commits = [line for line in log.stdout.strip().splitlines() if line]
    if len(commits) < 2:
        fail(f"expected at least 2 commits, found {len(commits)}. Make an initial commit and at least one follow-up commit.")

    messages = [m.strip() for m in run_git(["log", "--format=%s"], repo_dir).stdout.strip().splitlines() if m.strip()]
    for m in messages:
        if m.lower() in GENERIC_MESSAGES or len(m) < 10:
            fail(f"commit message '{m}' is too generic or short -- explain WHY the change was made, not just what changed.")

    tracked = run_git(["ls-files"], repo_dir).stdout
    if "digital_twin/classification.py" not in tracked.replace("\\", "/"):
        fail("digital_twin/classification.py is not tracked in the repository.")

    print(f"PASS: {len(commits)} commits found, all with descriptive messages; digital_twin/classification.py is tracked.")


if __name__ == "__main__":
    main()
