
# uniq


## 基本

入力はあらかじめ sort されている必要がある


## 重複していた行を表示

```
uniq -d
```


## 重複していた行数を表示

```
uniq -c
```


## 行の比較を最初の N 文字 で行う

```
uniq -w N
```

or

```
uniq --check-chars=N
```



