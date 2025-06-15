
# git merge type


## merge には 3種類 ある

- first foward
- 3 way
- squash


## default setting

```
wip:
```


## squash

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


## rebase merge ( 3 way ? )

wip:


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


