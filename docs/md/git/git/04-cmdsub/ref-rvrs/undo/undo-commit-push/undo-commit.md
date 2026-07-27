
# git commit  -  undo


## basic

- commit を 戻すのは `git reset --soft`


```
git reset --soft HEAD~
```

```
--soft  staged   の file 内容 を コマンド実行前の状態から 変更しない
        worktree の file 内容 を コマンド実行前の状態から 変更しない
```


## amend の代わりに reset する

```
git reflog

git reset --soft HEAD@{1}
```





