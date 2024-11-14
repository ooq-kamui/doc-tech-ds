
# git checkout


## 基本

基本は

- ある commit の file を worktree  へ取り出す

なのだが, 実質の用途としては,


- branch を指定した場合
  - branch 切り替え
    - 指定 branch の commit HEAD の 全 file が worktree ( , staged ? ) に取り出される
    - 現在の branch も 指定 branch になる


- commit を指定した場合
  - ある commit の file を worktree ( , staged ? ) へ取り出す

  - 指定 commit が HEAD の場合
    - worktree, staged の file の 変更 を 破棄



## branch 切り換え 用途

### branch を指定した場合は branch を切り替える

```
git checkout branch_name
```

自分としては,
branch の切り替え は頻繁にやらないのが無難 ( 慣れるまで )

dir ごとに, この dir は この branch と用途を決め, 動かさない

それよりも, 修正を破棄する用途に使用する


### branch 切り替え 強制

```
git checkout -f branch_name
```


### option

```
-b  新しい branch を作成, つまり, branch 作成もできる
```



## worktree 破棄 用途

### HEAD から取り出す

#### worktree, staged の file の変更を 取り消して, HEAD の file にする

```
git checkout HEAD -- file_path
```


#### worktree ( , staged ? ) の dir 配下の変更を 取り消して, HEAD の file 群にする

```
git checkout HEAD -- dir_path
```


#### worktree ( , staged ? ) の すべての変更を取り消して, HEAD の file 群にする

```
git checkout HEAD -- .
```


### staged から取り出す

#### worktree の file の変更を 取り消して, staged の file にする

```
git checkout -- file_path
```

つまり, commit 指定の省略は staged から取出し


### 特定 commit から取り出す

cmt_id01 の file01 を worktree ( , staged ? ) へ取り出す

現在の worktree の file01 は破棄される

```
git checkout cmt_id01 -- file01
```

commit_id は 同 branch history になくても, 同 repository のものであれば可



