
# grep


## 配下のファイルをぜんぶ対象

```
grep -nr "xxx" .
```

directory 指定で最後に / をつけると / が重複するので注意


## ファイル名を出力しない

```
grep -h xxx.txt
```


## file 拡張子 指定

```
grep -nr "xxx" --include "*.lua" .
```


## 単語検索

```
grep -nrw "xxx" .
```

```
[[:alnum:]]   英数字        [0-9A-Za-z]
[[:alpha:]]   英字          [A-Za-z]
[[:digit:]]   数字          [0-9]
[[:lower:]]   英字の小文字  [a-z]
[[:upper:]]   英字の大文字  [A-Z]
[[:blank:]]   space tab
[[:punct:]]   記号          !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
[[:xdigit:]]  16進数        [0-9A-Fa-f]
```


```
hilight color
export GREP_COLOR="1;32"
```

https://wiki.archlinux.jp/index.php/コンソールのカラー出力


```
color
Black         0;30
Blue          0;34
Green         0;32
Cyan          0;36
Red           0;31
Purple        0;35
Brown         0;33
Light Gray    0;37
Dark Gray     1;30
Light Blue    1;34
Light Green   1;32
Light Cyan    1;36
Light Red     1;31
Light Purple  1;35
Yellow        1;33
White         1;37
```

http://www.tldp.org/HOWTO/Bash-Prompt-HOWTO/x329.html



