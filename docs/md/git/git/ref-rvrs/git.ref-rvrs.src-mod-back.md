
# git ref rvrs  -  src mod back


## 途中まで開発したが, 一度 HEAD の内容に戻したい場合


### 現在の file を保存(退避)

staged を退避領域とする

```
git add file_path
```


### HEAD の内容を worktree に戻す

かつ, staged の file はそのまま

```
git restore --source HEAD --worktree file_path
```


### staged の内容を worktree に戻す

checkout で 引数の commit_id を省略すれば, staged から取り出すこと

```
git checkout -- file_path
```



