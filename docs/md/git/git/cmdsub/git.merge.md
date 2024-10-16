
# git merge


## 基本

別の branch ( の commit HEAD ) を 現在の branch へ取り込む

```
git merge branch_other
```


### 補足

`git pull` は `git fetch` + `git merge FETCH_HEAD`



## faq

`git merge` で

```
fatal: refusing to merge unrelated histories
```

が出た場合

```
git merge --allow-unrelated-histories target_branch
```

で いける



## git merge で vim を使う

```
git config --global core.editor vim
```


## merge で vimdiff を使う

https://scior.hatenablog.com/entry/2021/05/05/193113

git mergetoolを使う


```
git mergetool -t vimdiff
```

で, vimdiff を利用した編集となる

config に設定する場合は下記

```
git config --global merge.tool vimdiff
```

```
git mergetool
```


## git mergetool ( vimdiff ) の使いかた

上 : local / base / remote

下 : 作業中のファイル



## `.orig` file とは

git mergetool で編集後にできる backup file

とくに用途がなければ, rm してよい



## merge squash

複数 commit を 1 commit にまとめて merge する

ex

branch02 に branch01 に まだ merge されていない, 複数 commit があるとする

branch01 に移動

```
git checkout branch01
```

branch02 の 複数 commit を 1つ にまとめて merge

```
git merge --squash branch02
```


### 補足

`merge --squash` の対比として rebase merge というものについて 言及されることが ある


おさらい,
`git rebase` とは

派生 branch の 分岐点の commmit を 元 branch の 先端 に付け替える
こと

その上で,

rebase merge とは

```
git rebase --rebase-merge
```

か

```
git pull --rebase
```

のこと を指している

wip:



