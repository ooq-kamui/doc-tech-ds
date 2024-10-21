
# git restore


## 基本

worktree や staged の file を HEAD や 指定 commit の内容に戻す


2019 git 2.23 で `git switch`, `git restore` として 追加された

前は `git checkout` を駆使してやっていたことを 分かりやすい指定で できるようになった


## option なし の場合

```
git restore file_name
```

おそらく, worktree の file を HEAD の内容に戻す,
下記と同じ

```
git restore --source HEAD --worktree file_name
```

だが, この手の command は option, 引数 を 省略しないほうが無難



## worktree の file を HEAD の内容に戻す

```
git restore --source HEAD --worktree file_name
```


## staged の file を HEAD の内容に戻す

```
git restore --source HEAD --staged file_name
```


## worktree の file を 指定した commit の内容に戻す

```
git restore --source commit1 --worktree file_name
```


## ref

https://tracpath.com/docs/git-restore/



