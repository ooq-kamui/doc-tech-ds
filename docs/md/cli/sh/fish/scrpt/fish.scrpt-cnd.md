
# condition


## if

```
if test "$str1" = "$str2"

  echo $str1

end
```



## test

### 文字列

```
-z str              : str が 空文字
-n str              : str が 1文字以上

STRING1 =  STRING2  : STRING1 と STRING2 が同じ
STRING1 != STRING2  : STRING1 と STRING2 が異なる
```

ex

```
if test "$str1" = "$str2"
```

変数を見る 場合は, `""` で囲むのが無難,
あくまでも文字列の比較のため

`=` `!=` でも `test` は必要


### file, dir

```
-b FILE   ブロックデバイス
-c FILE   キャラクタデバイス
-d FILE   directory
-e FILE   path が存在する
-f FILE   通常の file
-g FILE   setgid アクセス権 を持つ
-G FILE   存在し, ユーザと同じグループIDである
-L FILE   シンボリックリンク
-O FILE   存在し, ユーザ所有である
-p FILE   名前付きパイプ
-r FILE   読み込み可能
-s FILE   file size が 0 より大きい ( 空ファイルではない )
-S FILE   ソケット
-t FD     端末である
-u FILE   setuidアクセス権を持つ
-w FILE   書き込み可能
          ただし、ファイルシステムが
          読み込み専用であることまではチェックしない
-x FILE   実行可能
```

### 整数関連

```
NUM1 -eq NUM2   NUM1 と NUM2 が同値
NUM1 -ne NUM2   NUM1 と NUM2 が同値ではない
NUM1 -gt NUM2   NUM1 >  NUM2 
NUM1 -ge NUM2   NUM1 >= NUM2 
NUM1 -lt NUM2   NUM1 <  NUM2 
NUM1 -le NUM2   NUM1 <= NUM2 
```

整数のみサポート


## and

```
if COND1 -a COND2
```

## or

```
if COND1 -o COND2
```

## not

```
if ! EXPRESSION
```

or

```
if not EXPRESSION
```


## 括弧で囲むことで 条件式をまとめられる

```
( EXPRESSION ) は EXPRESSION の値を返す
```

コマンド置換 として解釈されるのを防ぐために
\( とエスケープが必要



