
# doc-tech


## git

undo 的に write
- add ( staged )
- commit
- push


git reset


git rebase するなら, reset + stash + merge --ff のほうが無難では ?
- というより, rebase はこれの短縮 command と考えるのが妥当


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

- 上記を踏まえて, commit history tree image, write mod


git push
- case commit conflict
  - err msg
- push の前提


git rebase しなくても
- local の場合は, reset して, stash するほうが 手軽なのでは ??
  - というよりも, rebase は これの短縮 cmd です


faq
- 3way merge
  - parent が 2つ ある とはどういうことか?


git restore は rm ( del ) でできるのか? ( 同等か? )
- try ( confirm )


## github

chk rewrite re

github には pull req の merge で first forward はない
- これを踏まえた 一般的な flow
  - および pull req 時の merge type ごとの
    - 考察

github actions
- learn


## unix cmd

unix usr add grp


## vim

autocmd
- evnt lst
  - ggl


