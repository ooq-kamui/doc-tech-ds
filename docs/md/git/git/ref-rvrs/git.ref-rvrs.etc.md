
# git  -  ref rvrs


## 特定ファイルのみを 別 branch から取り込む

```
git checkout branch02_name -- file_path
```


## push してない commit があるか

```
git log origin/main..main
```


## git merge の vim で, 自分の .vimrc を適用したい

- そもそも, default で立ち上がっているのは vim ではなく, vi

なので,

```
git config --global core.editor vim
```

とする


## git merge で vimdiff を使う

```
git config --global merge.tool vimdiff
```

```
git mergetool
```


## git commit のあと, global の user, email を設定していなかったとき

```
git config --global user.name your_name
```

```
git config --global user.email you@example.com
```

```
git commit --amend --reset-author
```

confirm

```
git log
```


## git init したら, defautl branch が master だったとき

main に直したい場合

branch 名 変更

```
git branch -m master main
```


## ある commit の file list を表示する

```
git show commit_id --name-only
```



