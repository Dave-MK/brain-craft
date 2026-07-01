# Lab: Clean History

Lesson: `git-rebasing-basics` (boss battle)

## Setup

Run once: `python setup_repo.py`. It leaves you on
`improve-battery-thresholds`, which is 2 commits behind main.

## Task

1. Rebase `improve-battery-thresholds` onto the latest main
   (`git rebase main` or `git rebase master`, whichever your main branch
   is called).
2. Switch to main and merge the rebased branch in — it should now be a
   clean fast-forward, with **no merge commit**.
3. Run `python ../test_cases.py` to check your work.

If you instead just merge without rebasing first, the test will catch
it — a plain merge here would create a merge commit, which is exactly
what this lab is checking you avoided.
