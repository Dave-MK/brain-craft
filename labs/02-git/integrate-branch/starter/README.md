# Lab: Integrate the Branch

Lesson: `git-merging`

## Setup

Run once: `python setup_repo.py` — creates a baseline commit on your
main branch, plus an unmerged `new-thresholds` branch one commit ahead
of it.

## Task

1. Merge `new-thresholds` into your main branch.
2. Run `git log --graph --oneline` and check whether it was a
   fast-forward or a real merge commit — and be able to explain why.
3. Run `python ../test_cases.py` to check your work.
