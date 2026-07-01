# Lab: Resolve and Verify

Lesson: `git-resolving-conflicts`

## Setup

Run once: `python setup_repo.py`. Your main branch already has
`branch-a` merged in (`safe_limit_kw = 5200`). A second branch,
`branch-b`, changed the same line differently (`safe_limit_kw = 4900`)
and has not been merged yet.

## Task

1. Merge `branch-b` into your main branch. You will get a conflict on
   `digital_twin/classification.py`.
2. Resolve it: pick whichever value you think is more sensible (or a
   genuinely combined decision), and explain your reasoning in the
   merge commit message.
3. Remove **all** conflict markers, make sure the file is valid Python,
   and complete the merge.
4. Run `python ../test_cases.py` to check your work.
