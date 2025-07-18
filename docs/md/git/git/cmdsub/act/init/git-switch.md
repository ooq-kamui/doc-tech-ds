
# git switch


## 概要

git checkout よりも使いやすい cmdsub として登場

`git checkout` は `git switch` と `git restore` に分けられました



## branch list

```
git branch --list
```


## branch list  -  remote

リモート の ブランチ 一覧

```
git fetch
```

```
git branch -a
```


## branch を切り替える

```
git switch <branch-name>
```

- switch したとき, worktree の file は 変わらない ( 引き継ぐ )
- switch したとき, staged   の file は 変わらない ( 引き継ぐ )


## branch を新規作成して, それに切り替える

```
git switch -c <branch-name-new>
```


## `git switch` と `git checkout` の違い

git switch は worktree に変更があった場合に,
変更がそのままになる
, のかもしれない


## option

### 強制 実行

```
--discard-changes : staged, worktree の file が HEAD と異なる場合でも続行する
```

```
--force : --discard-changes の alias
```




