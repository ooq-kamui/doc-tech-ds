
# sed


## regex

```
-e      正規表現
-E  拡張正規表現
-r  拡張正規表現
```

## 実行結果 を 入力ファイル に 上書き保存 する

```
sed -i '' -e "s/srch/rpl/g" file_name.txt
```


## sed cmd

### 元の行 の 表示のみ

option -n と併用


m 行目を表示

```
sed -n "m p"
```


aa のある行から cc のある行まで を表示

```
sed -n "/aa/,/cc/ p"
```


### 削除

key1 のある行 を削除

```
sed "/key1/ d"
```


key1 のある行から key2 のある行 を削除

```
sed "/key1/,/key2/ d"
```


### 別ファイルの内容を差し込む

```
sed "/key/ r file.txt"
```

key の行の下の行に差し込まれる

key の行は消えない


### 置き換える文字を 1 char ずつ 定義

```
sed -e 'y|srch_char_lst|rpl_char_lst|'
```



## 位置指定

最後の行

```
sed "$ s/find/rpl/g"
```


m 行目 から n 行目

```
sed "m,n s/find/rpl/g"
```


m 行 のみ

```
sed "m s/srch/rpl/g"
```


key のある行

```
sed "/key/ s/find/rpl/g"
```


key1 のある行 から key2 のある行

```
sed "/key1/,/key2/ s/find/rpl/g"
```


## etc

置換後 の文字列に tab

```
t=$'\t'
```


置換後 の文字列に cr

```
LF=$(printf '\n_');LF=${LF%_}
```



