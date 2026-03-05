
# git commit

staged の内容を repo に反映する


## comment 付きで commit

```
git commit -m 'comment'
```


## 直前の commit を破棄して, 再 commit する

comment を修正したいとき に活用 が主

```
git commit --amend
```


## 直前の commit を破棄

```
git reset --soft HEAD~
```

`git reset` は `HEAD` の位置を戻すこと

`--soft` は worktree, staged はそのまま



## q

### `push` までしたあとに `git commit --amend` `git push` できる?

wip:


### `git commit --amend -m 'cmnt'` できる?

wip:



