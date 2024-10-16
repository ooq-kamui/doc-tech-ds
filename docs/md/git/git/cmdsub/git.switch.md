
# git switch

git checkout よりも使いやすい cmdsub として登場

`git checkout` は `git switch` と `git restore` に分けられました


## branch list

```
git branch
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
git switch branch_name
```


## branch を新規作成して, それに切り替える

```
git switch -c branch_name_new
```


## `git switch` と `git checkout` の違い

git switch は worktree に変更があった場合に,
変更がそのままになる
, のかもしれない



