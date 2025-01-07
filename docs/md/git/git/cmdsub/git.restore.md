
# git restore


## 基本

[ worktree / staged ] の file を [ HEAD / 指定 commit ] の内容にする ( 戻す )

HEAD の内容に戻すのが main 用途


worktree に file を取り出すのは git checkout のほうが馴染みがあるかもしれない,
という意味では,
staged の file を HEAD の file に戻すのが main 用途 ( かも )


2019 git 2.23 で `git switch`, `git restore` が追加された



## option なし の場合

慣れるまでは option, 引数 を 省略しないほうが無難
ですが,

```
git restore file_name
```

は ( おそらく ) 下記と同じ

worktree の file を HEAD の内容に戻す

```
git restore --source HEAD --worktree file_name
```



## source option のみ なし の場合

`--source` option は省略して, target option は指定することも可

だが, この場合, target によって source が変わる


### target が staged の場合

staged の file を HEAD の内容に戻す ( add を取り消す )

```
git restore --staged file_name
```

上記は下記と同

```
git restore --source HEAD --staged file_name
```


### target が worktree の場合

worktree の file を stage の内容に戻す

```
git restore --worktree file_name
```



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


## ref

https://tracpath.com/docs/git-restore/



