
# git  -  基本


## ref

学びたての場合,

- https://training.github.com/downloads/ja/github-git-cheat-sheet/
- https://www.atlassian.com/ja/git/tutorials/setting-up-a-repository/git-init

などが分かりやすい


## 基本概念

### 保存 領域

local だけで

- worktree   : 作業ファイル ( 開発するときに修正するファイル )
- staged     : add    で追加される
- repository : commit で追加される

の 3つがある


## 初級者が 誤解 混乱 しがちなこと

- branch は 枝 ( 木の枝 ) というよりは 撚り糸 のイメージ
- 分岐点 という言葉は誤解を生みやすい ( と思う )
  - 現在 ( local HEAD ) から commit history を過去に見たときの,  
    ( merge や push の対象 との ) 合流ポイント
  - ( push の場合 )  
    自分 ( local ) の commit history の中で,  
    そこ以降には 未 push がある,  
    そこ以前には 未 push がない ( remote と同一である ),  
    というポイント
  - pull req が merge されれば, 合流ポイントは 現在に近い方へ 移動する  
    ( その意味で, 木の枝 というよりは 撚り糸 のイメージ )
- commit 時間 と commit history の 順が 一致しない ( 前後している ) ことは  
  ふつうにあり得る
- github の推奨する workflow で考えたとき  
  pull ( merge ) の対象 branch と push の対象 branch は通常 異なる  
  が,  
  初級者への説明はこれを特に言明することなく 説明している場合がほとんど  
  というか,  
  workflow を踏まえた上で, pull ( merge ) や push の説明をしていることは ほとんどない  
  特に説明されないので, 初級者は 同じ branch として考えている  
  ( workflow によっては同じケースもあるので間違っているわけでもない )
  ( のだが, このため, 学習途中で必ず 疑問 混乱 が出てくる )
- 初級者への説明としては,  
  remote tracking branch は意識しなくてよいものとして, 説明されないのだが,  
  どう考えても, 最初から意識しておいたほうがよい


