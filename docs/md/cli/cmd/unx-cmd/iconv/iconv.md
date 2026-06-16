
# iconv


## cmd

```
iconv -f mb_code_fr -t mb_code_to file_name
```

```
cat file_name | iconv -f mb_code_fr -t mb_code_to
```

ex

```
cat file_name.txt | iconv -f sjis -t utf8 > file_name.utf8.txt
```


## option

### 変換できない文字を削除して続行

```
iconv -c
```


### mb_code の list

```
iconv -l
```

よく使うもの

```
utf8
sjis
euc-jp
```


