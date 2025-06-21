
# git restore


## 基本

- worktree または staged に行った修正を, 元の内容に 戻す
- file を個別に指定できる
- 何に戻すかを指定できる
  - worktree を戻す場合
    - HEAD ( 最新の commit 済 ) に戻す
    - staged に戻す
    - 特定 commit に戻す
  - staged を戻す場合
    - HEAD ( 最新の commit 済 ) に戻す
    - 特定 commit に戻す
- staged を HEAD に戻した場合, add が取り消される

捕捉

- worktree に関しては,  
  git checkout で,  
  HEAD から worktree への file 取り出し を行うことで,  
  同等のことを行える
- git restore は 2019 git 2.23 にて `git switch` とともに追加された


## worktree の file を HEAD の内容に戻す

```
git restore --source HEAD --worktree file_name
```


## staged の file を HEAD の内容に戻す

```
git restore --source HEAD --staged file_name
```


## worktree の file を 指定した commit の内容に戻す

```
git restore --source commit1 --worktree file_name
```


## option なし の場合

worktree の file を HEAD の内容に戻す

慣れるまでは option と 引数 を 明示指定する ほうが無難

```
git restore file_name
```

次と同じ

```
git restore --source HEAD --worktree file_name
```


## `--source` option は省略して, target option は指定した 場合

target が worktree の場合は, source が staged の file になるので注意

上記が本当か 確認したほうがよい


### target が staged の場合

staged の file を HEAD の内容に戻す

```
git restore --staged file_name
```

次と同じ

```
git restore --source HEAD --staged file_name
```


### target が worktree の場合

worktree の file を stage の内容に戻す

```
git restore --worktree file_name
```

上記で, source を staged に明示指定は可能か ?


## faq

- target が worktree のとき, staged の file に影響はない


## ref

https://tracpath.com/docs/git-restore/


