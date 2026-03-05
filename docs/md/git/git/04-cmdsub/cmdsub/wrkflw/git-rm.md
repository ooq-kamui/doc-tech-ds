
# git rm


## 基本

file を git の管理 ( 追跡 ) から 外す
( ための staged の操作 )


`git add` / `git rm` とは staged に対して, `add` / `rm` の意味


## file 指定

```
git rm file_name
```

このとき,

worktree から file は消える

staged の表示は `deleted` となる

file を ふつうに削除して, そのあと `git add` で `deleted` となるのと同じ


## dir 指定

dir 指定で, 配下の file すべて を対象

```
git rm -r dir_name/
```


## `--cached`

- `staged: new file`
- `staged: modified`

の file を `git rm` しようとすると, `--cached` option を促される

`--cached` option を指定すると, worktree に file が残る

ex

```
git rm --cached file_name
```


## notice

worktree だけから削除し, staged には残す option はない

これは, file をふつうに削除した状態と, 同じ


## ref

https://qiita.com/yusuke___web/items/d80a3adfe01086b4f62b

https://www.atlassian.com/ja/git/tutorials/undoing-changes/git-rm

https://tracpath.com/docs/git-rm/



