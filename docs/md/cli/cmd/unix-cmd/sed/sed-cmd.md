
# sed cmd


## `p`: 元の行 の 表示のみ

option -n と併用

m 行目を表示

```
sed -n "m p"
```


aa のある行から cc のある行まで を表示

```
sed -n "/aa/,/cc/ p"
```


## `d` 削除

key1 のある行 を削除

```
sed "/key1/ d"
```


key1 のある行から key2 のある行 を削除

```
sed "/key1/,/key2/ d"
```


## `r` 別ファイルの内容を差し込む

```
sed "/key/ r file.txt"
```

key の行の下の行に差し込まれる

key の行は消えない


## `y` 置き換える文字を 1 char ずつ 定義

```
sed -e 'y|srch_char_lst|rpl_char_lst|'
```


