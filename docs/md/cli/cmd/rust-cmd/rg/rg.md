
# rg  ( ripgrep )


## dir 指定

```
rg key dir
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


## file type を指定

```
rg ptn -g "*.lua" -g "*.md"
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


## cnf file

### cnf file name

`.ripgreprc`


### cnf file path setting

fish

```
set RIPGREP_CONFIG_PATH "$HOME/.ripgreprc"
```

bash

```
export RIPGREP_CONFIG_PATH="$HOME/.ripgreprc"
```

confirm

```
echo $RIPGREP_CONFIG_PATH
```


## ignore ( exclude ) 除外 関連 ( option )

### 基本

default で 隠しファイル ( .xxx ) は search 対象外

よって, `.gitignore` の内容も 対象外


### option

隠しファイル ( .xxx ) も search 対象とする

```
--hidden
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

https://zenn.dev/megeton/articles/56b8a6a74e6394



