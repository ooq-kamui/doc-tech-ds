
# faq  -  try confirm


## git push


### local branch から 違う remote branch に 直接 push することはできるのか ?

- やらないのが無難
- やろうと思えば できる

```
git push origin <local-branch-name>:<remote-branch-name>
```


## git pull ( merge from remote )


### 他の feat branch で 過去( HEAD よりも前 ) に commit された commit を pull して, 取り込むことはできるのか?

- できない
  - conflict がなくてもできない
  - こういう疑問自体, git の本当の基本は 3 way merge であることを理解していないことからくるもの
  - つまり, first forward merge のほうが 基本 と思っていることからきている疑問


#### 自 branch の状態: pull 対象 branch の HEAD よりあと: push までした

- `git merge --no--ff <branch-name>` ( 3 way merge ) でできる
  - が, 先端にも さらにあらたな commit ができる
  - git merge するとき, 先端に 新たな commit ( merge commit ) ができる, というのが git の 基本の挙動 です
  - というか, git merge は 先端に付けていく, というのが git の基本的な思想 です


#### 自 branch の状態: pull 対象 branch の HEAD よりあと: local commit まで

- この違いはあまり関係ないと思われる


