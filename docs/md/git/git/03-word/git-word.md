
# git word & concept


## branch

### upstream branch

- ある local branch において,  
  自分以外からの変更内容もすべて取り込むことを  
  前提としている remote branch
- git pull の実行で,  
  branch-name を省略したとき, default で pull 対象としている branch
- 確認方法
  - `git config --local --list` で  
    `branch.<branch-name>.remote=xxxx`
    `branch.<branch-name>.merge=xxxx`
    の値


### remote tracking branch

- remote branch と同じ内容のものとして, local 上にある branch
- fetch して, 最新状態を取り込む
- 通常 `origin/<branch-name>` で表現される
- `git branch -r` で remote tracking branch の list を表示


## merge

### merge

wip:


### rebase

wip:


## pull

### pull

- pull は 内部的には次をやっている
  - fetch
  - merge


## push

wip:




