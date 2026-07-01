"""Run this once to set up the baseline repo for this lab: python setup_repo.py"""

import subprocess

GIT_ENV = ["-c", "user.email=learner@braincraft.local", "-c", "user.name=BrainCraft Learner"]


def git(*args):
    subprocess.run(["git", *GIT_ENV, *args], check=True)


def main():
    git("init", "-q")
    git("add", "digital_twin/")
    git("commit", "-q", "-m", "Add initial digital_twin package: ingestion and classification")
    print("Baseline repo ready on main, with one commit.")


if __name__ == "__main__":
    main()
