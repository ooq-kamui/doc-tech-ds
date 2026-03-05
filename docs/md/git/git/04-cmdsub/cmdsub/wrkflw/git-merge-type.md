
# git merge type

ref

https://it-infomation.com/git-merge-ff-no-ff-squash/


## pull request 時の merge 3種

### first forward ( only )

```
git merge --ff-only <branch-name>
```

- `--ff` の場合,  
  first forward できない場合は, 3 way になる,  
  が, この option のことは いったん考えない


### squash

```
git merge --squash <branch-name>
```


### 3 way

```
git merge --no-ff <branch-name>
```


---

以下にそれぞれを記載する


## first forward ( only )

```
git merge --ff-only <branch-name>
```

- commit 順のとおりにそのまま merge する
- merge 先 に merge 元 にない commit がある場合,  
  何もしない

### image

merge 先に merge 元にない commit が ない

```
dev  : c1 - c2
              \
feat :         - c3 - c4

       git merge --ff-only feat

dev  : c1 - c2 - c3 - c4
```

merge 先に merge 元にない commit が ある

```
dev  : c1 - c2 - c5
              \
feat :         - c3 - c4

       git merge --ff-only feat

       何もしない

dev  : c1 - c2 - c5
              \
feat :         - c3 - c4
```


## squash

```
git merge --squash <branch-name>
```

- merge 元 の merge するべき 複数 commit を 1つ にまとめた 別の 1つの commit が作成される
- その commit を merge 先に merge する
- merge 元 には何もしない

### image

merge 先に merge 元にない commit が ない

```
dev  : c1 - c2
              \
feat :         - c3 - c4

       git merge --squash feat

dev  : c1 - c2 - s1
                 ( c3 + c4 )
              \
feat :         - c3 - c4
```

merge 先に merge 元にない commit が ある

```
dev  : c1 - c2 - c5
              \
feat :         - c3 - c4

       git merge --squash feat

dev  : c1 - c2 - c5 - s1
                      ( c3 + c4 )
              \
feat :         - c3 - c4
```


## 3 way ( --no-ff )

```
git merge --no-ff <branch-name>
```

- merge としての 新しい 1つ の commit を 作成する
- それを merge 先に merge する
- merge 元 としても それが HEAD になる ??  
  ( これが謎 なので いずれ確認する )

### image

merge 先に merge 元にない commit が ない

```
dev  : c1 - c2
              \
feat :         - c3 - c4

       git merge --no-ff feat

dev  : c1 - c2 ----------- t1
              \           /
feat :         - c3 - c4 -
```

merge 先に merge 元にない commit が ある

```
dev  : c1 - c2 - c5
              \
feat :         - c3 - c4

       git merge --no-ff feat

dev  : c1 - c2 - c5 ------ t1
              \           /
feat :         - c3 - c4 -
```


