
# git reset


## 基本

HEAD の位置を 戻す

戻す位置 ( commit ) は 引数で指定

このとき, worktree , staged の状態をどうするかも 指定できる


### 人間的な 主な用途

- 直近の commit を破棄する



### notice

指定する commit を `HEAD` にした場合,
`HEAD` の位置は変えずに,
`--hard`, `--mixed` の指定によって, worktree, staged の file を HEAD の内容に戻す,
という使いかたもできるが,

そういう使いかたはしないほうが, 無難

混乱が少ない

そういうときは, `git restore` を使う



## option

```
--soft  : HEAD を 指定した commit にする ( 戻す )

--hard  : HEAD を 指定した commit にする ( 戻す )
          worktree, staged も 変更
            変更していた場合, 破棄され
            指定した commit の内容 になる

--mixed : HEAD を 指定した commit にする ( 戻す )
          worktree は変更しない  
          staged   は変更
            変更していた場合, 破棄され
            指定した commit の内容 になる

option なし : --mixed

```


## --soft

HEAD を 指定した commit にする ( 戻す )  
worktree, staged は 変更しない

```
git reset --soft commit01
```


### --hard

HEAD を 指定した commit にする ( 戻す )  
worktree, staged も 変更  
  変更していた場合, 破棄され  
  指定した commit の内容 になる

```
git reset --hard commit01
```


### --mixed

HEAD を 指定した commit にする ( 戻す )  
worktree は変更しない  
staged   は変更  
  変更していた場合, 破棄され  
  指定した commit の内容 になる

```
git reset --mixed commit01
```



## 事例


### local で, 直前の commit を 破棄

```
git reset --soft HEAD~
```

補足

```
=  worktree, staged の状態はそのままで, HEAD を 1つ前の commit に戻す

=  --soft で worktree, staged は 変更しない

HEAD~ : 現在の HEAD ( の commit ) の 1つ前の commit
```



### remote で, 最新の commit を破棄して, 1つ戻す

```
git reset --hard HEAD~

git push -f origin main
```



### add ( staged ) を 破棄

```
git reset --mixed HEAD
```



### local を remote に強制的に合わせる

branch は main とする

```
git reset --hard origin/main
```



