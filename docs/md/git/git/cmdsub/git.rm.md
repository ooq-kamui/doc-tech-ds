
# git rm


## 基本

wip:


file or dir を worktree と staged から 削除 ( del ) する

git での追跡をやめる

git add と逆の動きをするもの


```
git rm -r dir_name/
```

```
git rm filen_name
```


worktree だけから削除し, staged には残す option はない



## 対象 dir 配下を git 管理から削除

```
git rm --cached -r dir_name/
```


## option

```
--cached : staged を削除, worktree はそのまま
```



## ref

https://qiita.com/yusuke___web/items/d80a3adfe01086b4f62b

https://www.atlassian.com/ja/git/tutorials/undoing-changes/git-rm

https://tracpath.com/docs/git-rm/



