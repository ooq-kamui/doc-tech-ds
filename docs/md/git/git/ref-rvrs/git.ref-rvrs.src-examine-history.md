
# git src examine history


## ある commit の file list を表示する

```
git show commit_id --name-only
```


## ある file の ( から ) commit history を表示する

```
git log file_path
```

diff あり

```
git log -p file_path
```

diff あり, 左右表示

```
git log --word-diff -p file_path
```


