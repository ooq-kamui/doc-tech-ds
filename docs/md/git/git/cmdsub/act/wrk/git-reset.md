
# git reset


## basic

- git reset で reset するものは commit
- HEAD の commit 位置 を 指定した ( 過去の ) commit 位置に 戻す
  - このとき, 直近の commit は破棄される  
    ( つまり reset )
- worktree と staged が変更されていた場合,  
  それぞれ どうするかを, 指定できる
- push していない commit に使用を留めるのが無難


## option

```
--soft      : worktree を変更していた場合
                特に何もせず, 変更はそのまま残る
              staged   を変更していた場合
                特に何もせず, 変更はそのまま残る

--mixed     : worktree を変更していた場合
                特に何もせず, 変更はそのまま残る
              staged   を変更していた場合
                変更は破棄され, 指定した commit の内容 に 戻る

--hard      : worktree を変更していた場合
                変更は破棄され, 指定した commit の内容 に 戻る
              staged   を変更していた場合
                変更は破棄され, 指定した commit の内容 に 戻る

option なし : --mixed

```

- commit の undo の意味では
  - `--mixed` にするのが妥当
  - worktree も戻したければ,  
    git reset 後, git restore で worktree を戻す ほうが 分かりやすい ( 概念として, たぶん )


## case use

### local で, 直前の commit を 破棄

```
git reset --soft HEAD~
```

- 補足
  - worktree, staged の状態はそのままで, HEAD を 1つ前の commit に戻す
  - `--soft` で worktree, staged は 変更しない
  - `HEAD~` : 現在の HEAD ( の commit ) の 1つ前の commit


### remote で, 最新の commit を破棄して, 1つ戻す

```
git reset --hard HEAD~
```

```
git push -f origin main
```


### add ( staged ) を 破棄

```
git reset --mixed HEAD
```

ただし, `git restore` を 使うほうが無難


### local の HEAD を remote に合わせる

`branch : main` とする

```
git reset --hard origin/main
```


## etc

指定する commit を `HEAD` にした場合,
`HEAD` の位置は変えずに,

`--hard`, `--mixed` の指定によって, worktree, staged の file を HEAD の内容に戻す,
という使いかたもできる

が,
その用途では `git restore` を使う ほうが無難 ( と思われる )


