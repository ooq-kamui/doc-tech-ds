
# git show


## ある commit の file list を表示する

```
git show --name-only <commit-id>
```


## head の file の内容 を 標準出力

```
git show HEAD:<file-path>
```


## head の file を nvim で見る

```
git show HEAD:<file-path> | nvim -
```


