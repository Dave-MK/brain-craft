"""python test_cases.py -- checks the Integrate the Branch lab."""

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

    branches_raw = run_git(["branch", "--list"], repo_dir).stdout
    branch_names = [b.strip().lstrip("* ") for b in branches_raw.strip().splitlines() if b.strip()]
    main_name = "main" if "main" in branch_names else ("master" if "master" in branch_names else None)
    if main_name is None:
        fail("could not find a main/master branch.")
    if "new-thresholds" not in branch_names:
        fail("expected a 'new-thresholds' branch from setup_repo.py -- did you run it?")

    is_ancestor = run_git(["merge-base", "--is-ancestor", "new-thresholds", main_name], repo_dir)
    if is_ancestor.returncode != 0:
        fail(f"'new-thresholds' has not been merged into {main_name} yet.")

    main_content = run_git(["show", f"{main_name}:digital_twin/classification.py"], repo_dir).stdout
    branch_content = run_git(["show", "new-thresholds:digital_twin/classification.py"], repo_dir).stdout
    if main_content != branch_content:
        fail(f"{main_name} does not contain new-thresholds' actual changes after the merge.")

    print(f"PASS: 'new-thresholds' is merged into {main_name}, and the change is present.")


if __name__ == "__main__":
    main()
