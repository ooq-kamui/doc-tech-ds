
# diff


## file name のみ表示

```
diff -rq a.md b.md
```


## 違いがある場合のみ msg を表示

```
diff -q a.md b.md
```



## 対象を 拡張子 で限定

```
wip: 難しそう
```



## git diff

```
git diff a.md b.md
```

option

```
-y  左右に並べて表示

-u  unified 形式
     違いのある箇所を1つにまとめて, - 記号 と + 記号 で変更箇所を示す
```



