
# git rm


## 基本

git での管理 ( 追跡 ) から file を削除する

```
git rm file_name
```

このとき,

worktree から file は消える

staged の表示は `deleted` となる

これは, file を ふつうに削除して, そのあと `git add` して `deleted` となるのと同じ


## dir 指定

dir 指定で, 配下の file すべて を対象

```
git rm -r dir_name/
```


## notice

worktree だけから削除し, staged には残す option はない

これは, file をふつうに削除した状態と, 同じこと

`git add` / `git rm` とは staged に対して, add / rm の意味 ( たぶん )



## worktree に file を残したい場合

wip: このあたり, 整理して書き直す


staged new file を取り消す

1度も commit されていない file,
つまり staged で new file の file の場合,

`--cached` option が必要 ( ないと err )

```
git rm --cached file_name
```

`--cached` option の意味としては ?

変更されている file の場合, worktree に残る


`--cached` は常に付けておくほうが無難



## ref

https://qiita.com/yusuke___web/items/d80a3adfe01086b4f62b

https://www.atlassian.com/ja/git/tutorials/undoing-changes/git-rm

https://tracpath.com/docs/git-rm/



