"""Run this once to set up a repo with a local 'origin' remote already
configured and pushed to: python setup_repo.py

There's no real GitHub here (this lab runs offline) -- a local bare
repository stands in for "origin," which is enough to practice push,
ls-remote, and the review-before-merge discipline the lesson teaches.
"""

import subprocess
import tempfile

GIT_ENV = ["-c", "user.email=learner@braincraft.local", "-c", "user.name=BrainCraft Learner"]


def git(*args, check=True):
    return subprocess.run(["git", *GIT_ENV, *args], check=check, capture_output=True, text=True)


def main():
    origin_path = tempfile.mkdtemp(prefix="braincraft-origin-")
    subprocess.run(["git", "init", "--bare", "-q", origin_path], check=True)

    git("init", "-q")
    git("add", "digital_twin/")
    git("commit", "-q", "-m", "Add initial digital_twin package: ingestion and classification")
    main_branch = git("branch", "--show-current").stdout.strip()

    git("remote", "add", "origin", origin_path)
    git("push", "-q", "-u", "origin", main_branch)

    print(f"Baseline ready: '{main_branch}' has one commit and is pushed to a local 'origin' remote at:\n  {origin_path}")


if __name__ == "__main__":
    main()
