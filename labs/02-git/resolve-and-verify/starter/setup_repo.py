"""Run this once to set up a guaranteed-conflict repo: python setup_repo.py"""

import subprocess

GIT_ENV = ["-c", "user.email=learner@braincraft.local", "-c", "user.name=BrainCraft Learner"]


def git(*args, check=True):
    return subprocess.run(["git", *GIT_ENV, *args], check=check, capture_output=True, text=True)


def set_safe_limit(value):
    with open("digital_twin/classification.py") as f:
        content = f.read()
    content = content.replace("safe_limit_kw=5000", f"safe_limit_kw={value}")
    with open("digital_twin/classification.py", "w") as f:
        f.write(content)


def main():
    git("init", "-q")
    git("add", "digital_twin/")
    git("commit", "-q", "-m", "Add initial digital_twin package: ingestion and classification")
    main_branch = git("branch", "--show-current").stdout.strip()

    git("branch", "branch-a")
    git("checkout", "-q", "branch-a")
    set_safe_limit(5200)
    git("commit", "-q", "-am", "Raise safe limit to 5200kW after equipment upgrade")
    git("checkout", "-q", main_branch)
    git("merge", "branch-a", "-q", "-m", "Merge branch-a: adopt raised safe limit")

    git("branch", "branch-b", main_branch + "~1")  # branch off the ORIGINAL commit, before branch-a's merge
    git("checkout", "-q", "branch-b")
    set_safe_limit(4900)
    git("commit", "-q", "-am", "Lower safe limit to 4900kW for a more conservative safety margin")
    git("checkout", "-q", main_branch)

    print(
        f"Baseline ready: '{main_branch}' already has branch-a merged (safe_limit_kw=5200). "
        "Merging branch-b will conflict on the same line."
    )


if __name__ == "__main__":
    main()
