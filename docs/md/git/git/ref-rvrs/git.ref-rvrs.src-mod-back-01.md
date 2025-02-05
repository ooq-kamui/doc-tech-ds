
# git ref rvrs  -  src


## staged file list

```
git diff --cached --name-only
```

or

```
git diff --staged --name-only
```



## push してない commit があるか

```
git log origin/main..main
```



## staged ( add ) を取り消す

staged を取り消す, とは  
staged の file を HEAD の内容に戻す, なので

```
git restore --staged file_path
```

上記は下記の省略形

```
git restore --source HEAD --staged file_path
```



## 特定ファイルのみを 別 branch から取り込む

```
git checkout branch02_name -- file_path
```



