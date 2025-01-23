
# git  -  src の修正を元に戻す


## push commit を巻き戻す

push までしてしまった場合, 基本的には, さらなる修正で直すほうが無難です
( どうしてもの場合を除けば )


local で commit を巻き戻す

```
git reset --hard commit_hash
```

remote に強制 push する

```
git push origin main -f
```


他の local で次を行う

```
git fetch origin main
```

```
git reset --hard origin/main
```



## `git commit --amend` したものが `push` 済 だった場合

local を remote と同じに戻す

```
git reset origin/main
```



