
# option  -  rg


## option の 引数 の書きかた

### 省略 opt

```
rg -g "*.lua"
```

### 省略しない opt

```
rg ptn --glob="*.lua"
```


---

## 大文字小文字の区別

```
-i  区別しない
-s  区別する
-S  smart
```


## 単語検索

```
rg -w ptn
```


## 隠しファイル ( .xxx ) も 検索対象 とする

```
--hidden
```


## file name のみ 出力

```
rg -l
```


## 行数表示しない

```
rg -N
```


## tag jmp 形式 で出力

file path 表示を 先頭の 1行にまとめない  
の意味

```
--no-heading
```


## or 検索

```
rg -e "ptn1" -e "ptn2" 
```

```
rg -e "ptn1|ptn2" 
```


## and 検索

option による and 検索はできない


## マッチしない行を 出力

```
--invert-match
```

```
-v
```


## arg 1 file でも, file name を表示

```
--with-filename
-H
```


## 実行時の option

```
--files  対象のファイルをすべて列挙する
--debug  どの設定ファイルで何が有効になったのか
--trace  どこで何がマッチしたのか?
```



