"""Run this once to set up the baseline repo for this lab: python setup_repo.py"""

import subprocess

GIT_ENV = ["-c", "user.email=learner@braincraft.local", "-c", "user.name=BrainCraft Learner"]


def git(*args, check=True):
    return subprocess.run(["git", *GIT_ENV, *args], check=check, capture_output=True, text=True)


def main():
    git("init", "-q")
    git("add", "digital_twin/")
    git("commit", "-q", "-m", "Add initial digital_twin package: ingestion and classification")

    main_branch = git("branch", "--show-current").stdout.strip()

    git("branch", "new-thresholds")
    git("checkout", "-q", "new-thresholds")
    with open("digital_twin/classification.py") as f:
        content = f.read()
    content = content.replace("warning_kw=4500", "warning_kw=4200")
    with open("digital_twin/classification.py", "w") as f:
        f.write(content)
    git("commit", "-q", "-am", "Experiment: lower warning threshold to 4200kW")
    git("checkout", "-q", main_branch)

    print(f"Baseline ready: '{main_branch}' has one commit; 'new-thresholds' has one unmerged commit ahead of it.")


if __name__ == "__main__":
    main()
