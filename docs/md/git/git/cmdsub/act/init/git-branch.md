
# git branch


## branch の list を表示

```
git branch
```


## remote の branch の list も表示

```
git fetch
```

のあと

```
git branch -a
```


## コミットの先端情報も表示する

```
git branch -v
```


## branch を作成

```
git branch branch_name
```


## branch name を変更する

```
git branch -m name_old name_new
```

ex

```
git branch -m master main
```


## branch を切り替える

branch の切り替えは `git branch` ではなく `checkout`, または `switch`

```
git checkout branch_name
```


## branch local を削除

```
git branch -d branch_name
```

- branch_name が push 済 の場合 local を削除する


## branch 強制削除

branch_name が push 済 でないが, 強制削除したいとき

```
git branch -D branch_name
```


## branch remote を削除

```
git push origin --delete branch_name
```


