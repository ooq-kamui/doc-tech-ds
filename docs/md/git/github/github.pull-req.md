
# git  -  pull-req


## 基本

pull req とは

remote 上で,
branch01 から branch02 に merge する
, その提案


## 一般的な 開発の流れ

- mainブランチから作業ブランチを切る
- ファイルを変更（実装などの作業をする）
- ファイルの変更をコミットする
- GitHubにpushをする
- プルリクエストを作る
- レビュー依頼をする
- 修正がある場合は修正をする
- approveをもらったらマージする
- ブランチを切り替える
- ローカルのmain(master)ブランチをリモートの最新と一致させる
- 1.で切った作業ブランチを削除する


## squash merge

### q

remote で pull req から squash merge された場合
local で その branch を 継続して 利用できる ?

### a

できるかどうかは調査中ですが,

仮にできたとしても,
commit history の意味がわからなくなるので,
使用しないのが無難,
と思われる


## ref

- https://qiita.com/kuuuuumiiiii/items/42d2d9ed11e3b29c22cf
- https://zenn.dev/gachigachi/articles/dcd833c56bd0ed



