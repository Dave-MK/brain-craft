"""Run this once: python setup_repo.py

Sets up a feature branch that has fallen behind main by two commits --
the exact situation a rebase is for.
"""

import subprocess

GIT_ENV = ["-c", "user.email=learner@braincraft.local", "-c", "user.name=BrainCraft Learner"]


def git(*args, check=True):
    return subprocess.run(["git", *GIT_ENV, *args], check=check, capture_output=True, text=True)


def append_comment(comment):
    with open("digital_twin/classification.py", "a") as f:
        f.write(f"\n# {comment}\n")


def main():
    git("init", "-q")
    git("add", "digital_twin/")
    git("commit", "-q", "-m", "Add initial digital_twin package: ingestion and classification")
    main_branch = git("branch", "--show-current").stdout.strip()

    git("checkout", "-q", "-b", "improve-battery-thresholds")
    with open("digital_twin/classification.py") as f:
        content = f.read()
    content = content.replace("warning_kw=4500", "warning_kw=4300")
    with open("digital_twin/classification.py", "w") as f:
        f.write(content)
    git("commit", "-q", "-am", "Lower battery warning threshold to 4300kW")

    git("checkout", "-q", main_branch)
    append_comment("Unrelated: logged for audit trail after infra review")
    git("commit", "-q", "-am", "Add audit-trail comment after infra review")
    append_comment("Unrelated: second infra-driven note")
    git("commit", "-q", "-am", "Add second audit-trail comment")

    git("checkout", "-q", "improve-battery-thresholds")

    print(
        f"Baseline ready: 'improve-battery-thresholds' has 1 commit and is now 2 commits "
        f"behind '{main_branch}'. You are currently on 'improve-battery-thresholds'."
    )


if __name__ == "__main__":
    main()
