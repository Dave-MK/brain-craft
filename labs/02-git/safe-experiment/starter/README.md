# Lab: Safe Experiment

Lesson: `git-branches`

## Setup

Run once: `python setup_repo.py` — creates a baseline repo on `main` with
one commit.

## Task

1. Create a new branch (e.g. `new-thresholds`).
2. On that branch, change `warning_kw`'s default in
   `digital_twin/classification.py` to a different value and commit it.
3. Switch back to `main` and confirm the file there is unchanged.
4. Stay on `main` when you're done.
5. Run `python ../test_cases.py` (or copy `test_cases.py` in here and run
   it directly) to check your work.
