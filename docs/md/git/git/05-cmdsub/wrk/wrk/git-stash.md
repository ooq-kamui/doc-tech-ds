
# git stash


## 基本

変更 ( worktree ) を 退避し,  
git pull 後,  
退避した file を元に戻す  
ことができる


基本的には下記の流れで 実行すれば 問題ない

```
git stash list            # 確認

git stash push 'comment'

git stash list            # 確認

git status                # 確認

git pull origin main

git stash pop

git stash list            # 確認

git status                # 確認
```

pop 時に conflict があると, stash は 自動で drop されない  
手動で conflict 解消後,

```
git stash drop
```

で 削除する


## stash された stash list を表示する

```
git stash list
```

## stash された file list を表示

```
git stash show <stash-no>
```


## worktree を stash

```
git stash push
```

or

```
git stash push 'comment'
```


## stash されたファイルを復元

### 直近に stash された file を復元

```
git stash pop
```

### stash-no を指定して 復元

```
git stash apply stash@{no}
```

stash は破棄されない


### stash された file のうち, 指定した file を復元

```
git checkout stash@{no} file_path
```

stash は破棄されない


## stash を破棄

### 直近に 保存された stash を破棄

```
git stash drop
```

### stash-no を指定して 破棄

```
git stash drop stash@{no}
```


## err sample

worktree の変更を commit せずに
pull しようとすると,  
下記のエラーとなる

```
error: Your local changes to the following files would be overwritten by merge:
        path/to/file
Please, commit your changes or stash them before you can merge.
Aborting
```

message にあるように, このときに stash を活用する


