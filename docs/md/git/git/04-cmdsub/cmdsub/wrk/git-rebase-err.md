
# git rebase  -  err


## git rebase で conflict があったとき

```
Auto-merging doc/try/t00.md
CONFLICT (content): Merge conflict in doc/try/t00.md
error: could not apply d334df5... t02
hint: Resolve all conflicts manually, mark them as resolved with
hint: "git add/rm <conflicted_files>", then run "git rebase --continue".
hint: You can instead skip this commit: run "git rebase --skip".
hint: To abort and get back to the state before "git rebase", run "git rebase --abort".
Could not apply d334df5... t02
```


## `git pull --rebase` で conflict が起きた

```
hint: Resolve all conflicts manually, mark them as resolved with
hint: "git add/rm <conflicted_files>", then run "git rebase --continue".
hint: You can instead skip this commit: run "git rebase --skip".
hint: To abort and get back to the state before "git rebase", run "git rebase --abort".
hint: Disable this message with "git config set advice.mergeConflict false"
```








