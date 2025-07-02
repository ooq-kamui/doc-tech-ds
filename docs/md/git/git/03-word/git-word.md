
# git word & concept


## branch

### upstream branch

- ある local branch において,  
  自分以外からの変更内容もすべて取り込むことを  
  前提としている remote branch
- git pull の実行で,  
  branch-name を省略したとき, default で pull 対象となる branch
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


## origin とは

remote name のこと  
らしいが,  
origin 以外に見たことがないので, いったん深く考えない  
とにかく remote のこと


## commit

wip:


## merge

別の branch の commit を 自分の branch へ取り込む こと

```
git merge <branch-name>
```

### 補足

`git pull` は

- `git fetch`
- `git merge FETCH_HEAD`

をやっている


## rebase

first forward merge ができないときに,  
自分の側の 未 push commit を いったん棚上げし ( stash 相当の状態 ),  
merge して,  
棚上げした commit を commit history の先端に付け替えること
( push 時に err とならない状態にすること )


慣れるまでは,  
local の 未 push commit を reset し,  
push 直前に 再 commit するほうが,  
やっていることが分かりやすいので, それを推奨


## pull

- pull は 内部的には次をやっている
  - fetch
  - merge


## push

( 確証ないが 現段階の自分の理解 )

- remote を local の内容で update すること
- 基本的には, ( remote 側から見て ) first forward merge するのと同じ状況でなければ  
  err になる
- ただし, 強制 push することもできる


