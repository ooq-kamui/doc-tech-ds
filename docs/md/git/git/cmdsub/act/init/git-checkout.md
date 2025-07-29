
# git checkout


## 基本

worktree へ file を取り出す

このとき, 実行前の worktree file は破棄される

このとき, staged の file も 基本的には 破棄 される  
ただし, staged から 取り出す場合は, staged は 破棄 されない  
( 当然といえば当然だが )


## HEAD から取り出す

### file 指定 の場合

```
git checkout HEAD -- file_path
```

- worktree の 変更は 破棄 される
- staged   の 変更も 破棄 される


### dir 指定 の場合

```
git checkout HEAD -- dir_path
```

- worktree の 変更は 破棄 される
- staged   の 変更も 破棄 される

ex

カレント dir 配下 すべて

```
git checkout HEAD -- .
```


## staged から取り出す

commit_id を指定しない

```
git checkout -- file_path
```

- worktree の file の 変更 は 破棄される
- staged   の file は 維持 される  
  ( staged からの取り出しなので, 当然ではある )



## 指定 commit から取り出す

cmt_id_01 の file_01 を worktree ( , staged ? ) へ取り出す

```
git checkout cmt_id_01 -- file_01
```

- worktree の file は 破棄 される
- staged   の file は 破棄 される ? : todo confirm
- commit_id は 同 branch history になくても, 同 repository の commit_id であれば可


## 指定 branch から取り出す

```
git checkout <branch-name> -- file-path
```

おそらく,  
指定 branch の HEAD の commit を対象とする 動き : todo confirm


## 補足

下記の用途でも, かつては `git checkout` を使用していましたが..

- branch 切り換えは, 現状は, `git switch` を使うのが 無難です
- branch 新規作成は, 実運用上は, remote ( github など ) で作成するのが 無難です



