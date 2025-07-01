
# git  -  基本


## 基本概念

### 保存 領域

local だけで

- worktree   : 作業ファイル ( 開発するときに修正するファイル )
- staged     : add    で追加される
- repository : commit で追加される

の 3つがある


## question

### origin とは

remote name とのことだが,  
origin 以外に見たことがないので, いったん深く考えない


## ref

学びたての場合,

- https://training.github.com/downloads/ja/github-git-cheat-sheet/
- https://www.atlassian.com/ja/git/tutorials/setting-up-a-repository/git-init

などが分かりやすい


## notice

初級者が 誤解しがちなこと
- branch 枝 ( 木の枝 ) > というよりは 撚り糸 のイメージ
- 分岐点 > 分岐点 という言葉はかなり誤解を生みやすいと思う  
  - 現在 ( HEAD ) から過去を見たときの,  
    ( upstream branch への ) 合流ポイント
  - 単に  
    自分 ( local ) の commit history の中で,  
    そこ以降には 未 push がある,  
    そこ以前には 未 push がない ( 同一である ),  
    というポイント
  - pull req が merge されれば, 位置は 変動する, 現在に近い方へ

- 初級者は 開発者として 読んでいるとして,  
  何 flow の 開発者なのか を明示した上で,  
  現実的に一般的な状況に則って, 説明してほしい

- commit 時間 と commit history の 順が 一致しない ( 前後している ) ことは  
  ふつうにあり得る ということ







