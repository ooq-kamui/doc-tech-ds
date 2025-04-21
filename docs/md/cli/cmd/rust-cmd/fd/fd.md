
#  fd


## ref

https://zenn.dev/megeton/articles/c408511c66f45d


## install

```
brew install fd
```


## arg

```
fd ptn dir
```


## option

```
-e               拡張子指定
                 複数の場合は -e も複数指定

-t               ファイルタイプ指定

-I               .gitignore, .ignore, .fdignore を含める

-H  --hidden     隠しファイル ( . から始まるファイル名 ) を対象にする

-E               除外パターン

-L  --follow     symbolic link を対象にする

-d  --max-depth  max depth
```


```
sort option : 不明 ( ない? )
```


## ptn

正規表現が使える


or 指定

```
fd 'aaa|bbb'
```


