
# git init


## まっさらな local から repository を新規作成

### 初回

repository cre から push まで

local repository を作成

```
git init
```

commit 対象ファイルに add

```
git add xxx.txt
```

commit 対象ファイルを commit

```
git commit -m "comment"
```

追加した staged ( ファイルの変更点 ) をGitHubに作成

```
git remote add origin github-url
```

ローカルリポジトリのファイルをGitHubのリポジトリに送信 ( push )

```
git push origin master
```


### 2回目以降

修正 file の push まで

staged に add ( commit 対象 file にする )

```
git add xxx.txt
```

staged に add された file ( commit 対象 file ) を commit

```
git commit -m "comment"
```

push ( commit された file を github に upload )

```
git push origin master
```


## repository の状態を確認

```
git status
```



## すでにある dir 配下の file 群を repository 化する

prj dir に移動

```
cd prj-dir
```

リポジトリを作成

```
git init
```

.git という dir が作成される

確認

```
git status
```

git で管理されていない file が表示される

エラーが発生しなければ ok


.gitignore を作成

```
vi .gitignore
```

対象から除外する file や dir を 記述して保存


.gitignore に登録したもの以外 の file をまとめて stage に add する

```
git add -A
```


### commit

commit msg つきで commit

```
git commit -m "new"
```

commit msg をつけない場合

```
git commit ???
```


### 追加した staged  ( ファイルの変更点 ) を github に作成

github の repository と紐づける

```
git remote add origin https://github.com/ooq-kamui/cnf
```

github に repository を作成

```
github.com の ui 上から作成する
```


### push

push

```
git push origin master
```



---

## etc

git で管理されているファイルを確認する

```
git show
```



前回から変更されたファイルを確認する

```
git status
```

commit 済 の file をさらに編集したときに  
commit 済 の file だけを 再度 staged に add, commt する

```
git commit -a -m "[msg]"
```



---

## worktree の変更をなしにする

staged から戻す

```
git checkout filename
```



---

## pw 変更した場合

```
git config --global user.name  "kamui"
git config --global user.email "ooq-kamui@gmail.com"
```

など 上記でなおった ( くわしくはよくわからず)



再度 push

```
git push origin master   # HEAD でも可? ( よくわからず )
```



???
```
Username for 'https://github.com': ooq-kamui
Password for 'https://donchan922@github.com': pw を入力
```



