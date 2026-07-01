"""python test_cases.py -- checks the Safe Experiment lab."""

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

    experiment_branches = [b for b in branch_names if b != main_name]
    if not experiment_branches:
        fail("no branch besides main found -- did you create a new branch for your experiment?")
    experiment_branch = experiment_branches[0]

    only_on_branch = run_git(["log", f"{main_name}..{experiment_branch}", "--oneline"], repo_dir).stdout.strip()
    if not only_on_branch:
        fail(f"'{experiment_branch}' has no commits beyond {main_name} -- did you commit your experimental change on it?")

    main_content = run_git(["show", f"{main_name}:digital_twin/classification.py"], repo_dir).stdout
    branch_content = run_git(["show", f"{experiment_branch}:digital_twin/classification.py"], repo_dir).stdout
    if main_content == branch_content:
        fail(f"digital_twin/classification.py is identical on {main_name} and {experiment_branch} -- did you actually change something on the branch?")

    current_branch = run_git(["branch", "--show-current"], repo_dir).stdout.strip()
    if current_branch != main_name:
        fail(f"you should end this lab on {main_name} to prove it wasn't affected by the experiment (currently on '{current_branch}').")

    print(f"PASS: '{experiment_branch}' has its own commit and its own change, and {main_name} is untouched.")


if __name__ == "__main__":
    main()
