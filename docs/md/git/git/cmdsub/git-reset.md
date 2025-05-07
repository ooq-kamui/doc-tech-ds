
# git reset


## 基本

直近の commit を破棄し

HEAD の commit 位置 を 以前のものに戻す

- worktree
- staged

が変更されていた場合, それぞれ どうするかを, 指定できる


ただし,
push していない commit に使用を留めるのが無難


### notice

指定する commit を `HEAD` にした場合,
`HEAD` の位置は変えずに,

`--hard`, `--mixed` の指定によって, worktree, staged の file を HEAD の内容に戻す,
という使いかたもできる

が,
その用途では `git restore` を使う ほうが無難 ( と思われる )


## option

```
--soft  : HEAD を 指定した commit に 戻す
          worktree を変更していた場合
            特に何もせず, 変更はそのまま残る
          staged   を変更していた場合
            特に何もせず, 変更はそのまま残る

--hard  : HEAD を 指定した commit に 戻す
          worktree を変更していた場合
            変更は破棄され, 指定した commit の内容 に 戻る
          staged   を変更していた場合
            変更は破棄され, 指定した commit の内容 に 戻る

--mixed : HEAD を 指定した commit に 戻す
          worktree を変更していた場合
            特に何もせず, 変更はそのまま残る
          staged   を変更していた場合
            変更は破棄され, 指定した commit の内容 に 戻る

option なし : --mixed

```


## --soft

- HEAD を 指定した commit に 戻す
- worktree を変更していた場合
  - 特に何もせず, 変更はそのまま残る
- staged   を変更していた場合
  - 特に何もせず, 変更はそのまま残る

```
git reset --soft commit01
```


### --hard

- HEAD を 指定した commit に 戻す
- worktree を変更していた場合
  - 変更は破棄され, 指定した commit の内容 に 戻る
- staged   を変更していた場合
  - 変更は破棄され, 指定した commit の内容 に 戻る

```
git reset --hard commit01
```


### --mixed

- HEAD を 指定した commit に 戻す
- worktree を変更していた場合
  - 特に何もせず, 変更はそのまま残る
- staged   を変更していた場合
  - 変更は破棄され, 指定した commit の内容 に 戻る

```
git reset --mixed commit01
```


## 事例

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


