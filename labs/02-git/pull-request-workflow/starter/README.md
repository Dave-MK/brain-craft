# Lab: Pull Request Workflow

Lesson: `git-remote-collaboration`

## Setup

Run once: `python setup_repo.py` — creates a repo with a local `origin`
remote already configured and pushed to. (This lab runs offline, so a
local bare repository stands in for a real GitHub remote — enough to
practice push, `ls-remote`, and the review-before-merge discipline.)

## Task

1. Create a branch, make a real change to `digital_twin/classification.py`,
   and commit it.
2. Push that branch to `origin`.
3. Write a `PULL_REQUEST.md` file in this folder with:
   - A description of what changed and why.
   - A "Reviewer checklist" section with at least two specific things a
     reviewer should check (as a markdown list).
4. Run `python ../test_cases.py` to check your work.
