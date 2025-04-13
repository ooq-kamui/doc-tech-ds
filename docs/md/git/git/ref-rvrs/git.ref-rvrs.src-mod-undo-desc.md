
# git ref rvrs  -  src mod back  -  desc


## ref

https://www.atlassian.com/ja/git/tutorials/undoing-changes



## 概要

- git checkout
  - ある commit の file 内容 を worktree に取り出す
  - 実行された commit を修正したりするわけではない
  - file, dir 個別指定 できる


- git restore
  - worktree / staged の file 内容 を HEAD の内容に戻す
  - 実行された commit を修正したりするわけではない
  - 対象 commit を 現在の HEAD とした git checkout, のようなもの
  - file 個別指定 できる
    - というか, file 個別指定 しかできない ?
      - 全体を戻したい場合は reset を使用 ( たぶん )

- git reset
  - 指定した commit の状態へ, HEAD, worktree, staged を戻す
    - wip: ここを詳しく記述すること  
      どういう意味か  
      file 内容を戻す意味なら, そのように明記する
  - 実行された commit を修正したりするわけではない


- git commit --amend
  - 直前の commit を破棄して, 再 commit


使用度 低

- git rebase
  - commit 履歴を変更する

- git revert
  - commit を削除する新しい commit を作成する



## 基本 方針

基本的には, commit をやり直したいことが多い ( と思う )

push 前, で, 1つ前の commit の修正 であれば, git commit --amend で修正する

push 前, で, 2つ以上前の commit の修正は, さらなる commit で修正するほうが無難です

push 後, の場合は, さらなる commit で修正するほうが無難です


