
# 逆引き


## dir 指定

```
rg ptn dir
```


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


## file name のみ 出力

```
rg -l
```


## file name を 出力しない

```
rg --no-filename
```

```
rg -I
```


## 各行に file name を出力

```
rg --with-filename
```

```
rg -H
```


## 行数を出力 しない

```
rg --no-line-number
```

```
rg -N
```


## 行数を出力 する

```
rg --line-number
```

```
rg -n
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

option による複数単語指定はできない

```
rg 'key1.+key2'
```

のように 正規表現で指定する

順番固定となるが 諦める


## マッチしない行を 出力

```
--invert-match
```

or

```
-v
```


## 空行 ( 空白行 ) を出力しない

```
rg -v -e '^[ \t]*$'
```


## 対象 file 数 の count

fish

```
rg ptn -l | count
```


## 実行時の option など の確認

```
--files  対象のファイルをすべて列挙する
         そもそもファイル見てんのか? のとき
--debug  どの設定ファイルで何が有効になったのか
--trace  どこで何がマッチしたのか?
```


## file name 一括置換

```
rg 'Apple' -l | xargs sd 'Apple' 'Google'
```


## vim から call するための option

```
--vimgrep
```

vim で :grep で ripgrep 実行

```
if executable('rg')
    let &grepprg = 'rg --vimgrep'
    set grepformat=%f:%l:%c:%m
endif
```


## ref

https://qiita.com/takiguchi-yu/items/1a3ecb3f103f5239fb04


