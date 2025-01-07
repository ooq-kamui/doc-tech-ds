
# git checkout


## 基本

worktree へ file を取り出す

このとき, 実行前の worktree file は破棄される

このとき, staged の file が 破棄されるか, 維持されるか は 引数の指定 による

( staged から 取り出す, 以外は, staged は 破棄される, かも ? ( 考えてみれば 当然 .. ? ) )


## HEAD から取り出す

### file 指定 の場合

```
git checkout HEAD -- file_path
```

- worktree の 変更は破棄される
- staged   の 変更も破棄される


### dir 指定 の場合

```
git checkout HEAD -- dir_path
```

- worktree の 変更は破棄される
- staged   の 変更も破棄される

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

- worktree の file の変更は 破棄される
- staged   の file は維持される  
  ( staged からの取り出しなので, 当然ではある )



## 指定 commit から取り出す

cmt_id_01 の file_01 を worktree ( , staged ? ) へ取り出す

```
git checkout cmt_id_01 -- file_01
```

- worktree の file は破棄される
- staged   の file は破棄される ? todo confirm
- commit_id は 同 branch history になくても, 同 repository の commit_id であれば可



## 補足

下記の用途でも, かつては `git checkout` を使用していましたが..

- branch 切り換えは, 現状は, `git switch` を使うのが 無難です
- branch 新規作成は, 実運用上は, remote ( github など ) で作成するのが 無難です



