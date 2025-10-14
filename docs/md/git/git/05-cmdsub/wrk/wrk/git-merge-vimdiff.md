
# git merge vimdiff


## git merge で vim を使う

```
git config --global core.editor vim
```


## merge で vimdiff を使う

ref https://scior.hatenablog.com/entry/2021/05/05/193113

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


