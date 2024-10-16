
# .gitignore


## 確認方法

### ignore されているかを確認

```
git status --ignored
```

git status と見比べて 確認


### ignore されている file を表示

```
git ls-files --other --ignored --exclude-standard
```


## 基本

### .gitignore file cre

```
vi .gitignore
```

管理対象から除外する file, dir を 記述して save


## format

### comment

```
# で始まる行はcomment
```


### 配下すべての file.txt ファイル

```
file.txt
```


### 配下すべての dir/ ディレクトリ の配下

```
dir/
```


### wild card 指定で 指定できる

```
hoge.*.ogg
```


### 拡張子で除外

```
*.ogg
```


### 配下のすべての dir/ 配下の特定拡張子のファイル

```
dir/**/*.ts
```


### 絶対パスで file 指定

```
/aaa/bbb/ccc/file.txt
```


### 絶対パスで dir 指定

```
/aaa/bbb/ccc/dir/
```


### ただし, この file は 除外しない

```
!/file.txt
```


## あとから .gitignore に 追加して, 管理対象から除外する

.gitignore に file, dir を 追記

```
vi .gitignore
```

.gitignore にあとから設定しても  
既にリポジトリに登録されているものはリポジトリに残ったままとなる  

このため, 下記の `管理対象から除外` を実行する


## 管理対象から除外

file を除外する

```
git rm --cached filename
```

file を複数指定することも可


dir を除外する

```
git rm --cached -r dirname
```

commit, push まで実行する


```
> [!!]  
> 先に file を del して push してしまった場合  
> 上記の方法でも github の history からは消えない ( 気がする )
> これをちゃんとする方法を調べる
```



