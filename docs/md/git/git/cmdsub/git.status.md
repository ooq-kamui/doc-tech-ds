
# git status


https://git-scm.com/docs/git-status


## status ( 現在の状態 ) を表示 ( 確認 )

- staging されている file  
  `>` add 済, commit 未 の file  
  staged と HEAD ( repo ltst ) に違いがある file

- staging されていない file  
  `>` add 未 file ( mod / del )  
  worktree と staged に違いがある file

- 未追跡の file  
  `>` add 未 file ( new )  
  git によって追跡されない ( かつ .gitignore で無視されない ) worktree の file

が表示される

```
git status
```


## 短い形式で表示する

```
git status -s
```

```
git status -- short
```


## 補足

`git status` は いったん 上記くらい の理解でよい と思います



