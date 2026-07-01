"""python test_cases.py -- checks the Clean History lab."""

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
    if "improve-battery-thresholds" not in branch_names:
        fail("expected an 'improve-battery-thresholds' branch from setup_repo.py -- did you run it?")

    is_ancestor = run_git(["merge-base", "--is-ancestor", "improve-battery-thresholds", main_name], repo_dir)
    if is_ancestor.returncode != 0:
        fail(f"'improve-battery-thresholds' has not been merged into {main_name} yet.")

    merges = run_git(["log", "--merges", "--oneline", main_name], repo_dir).stdout.strip()
    if merges:
        fail(
            "a merge commit was found on your main branch -- this means you merged "
            "improve-battery-thresholds without rebasing it onto main first. Reset and "
            "rebase before merging so the result is a clean fast-forward."
        )

    content = run_git(["show", f"{main_name}:digital_twin/classification.py"], repo_dir).stdout
    if "warning_kw=4300" not in content:
        fail("main does not contain the threshold change from improve-battery-thresholds after the merge.")

    print(f"PASS: '{main_name}' contains the rebased change via a clean fast-forward, no merge commit.")


if __name__ == "__main__":
    main()
