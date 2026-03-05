
# git restore


## 基本

- worktree または staged に行った修正を, 元の内容に 戻す
- file を個別に指定できる
- 何を 何に 戻す か を指定できる
  - worktree を戻す 場合
    - HEAD ( 最新の commit 済 ) に戻す
    - staged に戻す
    - 特定 commit に戻す
    - 捕捉
      - git checkout で, HEAD から worktree への file 取り出し を行うことで,  
        同等のことを行える
  - staged   を戻す 場合
    - HEAD ( 最新の commit 済 ) に戻す
    - 特定 commit に戻す
    - 捕捉
      - staged を HEAD に戻した場合, add が取り消される

捕捉

- git restore は 2019 git 2.23 にて `git switch` とともに追加された


## target : worktree


### HEAD        の内容に戻す

```
git restore --worktree --source HEAD    file_name
```


### 指定 commit の内容に戻す

```
git restore --worktree --source commit1 file_name
```


## target : staged

### HEAD        の内容に戻す

```
git restore --staged   --source HEAD    file_name
```

### 指定 commit の内容に戻す

```
git restore --staged   --source commit1 file_name
```


## option を省略した とき

- 慣れるまでは option と 引数 を 明示指定する ほうが無難 です

基本は

- target を省略した とき, target : `--worktree`
- source を省略した とき, source : `HEAD`


### 以下, 組み合わせで記す

- `git restore              --source HEAD   file_name`
  - 次と同じ  
    `git restore --worktree --source HEAD   file_name`

- `git restore                              file_name`
  - 次と同じ  
    `git restore --worktree --source HEAD   file_name`

- `git restore   --worktree                 file_name`
  - 次と同じ  
    `git restore --worktree --source staged file_name`
    - target が worktree の場合は, source が staged になるので 注意 ???
      - 要確認 !!!

- `git restore   --staged                   file_name`
  - 次と同じ  
    `git restore --staged   --source HEAD   file_name`


## faq

- target が worktree のとき, staged の file に影響はない


## ref

https://tracpath.com/docs/git-restore/


