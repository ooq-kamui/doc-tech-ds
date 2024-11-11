
# list ( array )


## 変数が配列かどうか

```
Array.isArray(ar1)
```


## 要素の追加

```
ar = [];
b = "b";

ar.push(b);
```

- 元配列 を 変更
- return : 要素数


## array の連結

```
ar3 = ar1.concat(ar2);
```

- 元配列 を 変更しない
- return : 新規 配列


## 要素の削除

```
ar.splice(削除する要素のidx, 削除する要素の個数)
```

- 元配列 を 変更
- return : 取り除かれた要素を含む配列


## 要素 を filter した 新しい 配列

```
ar2 = ar1.filter((val, idx) => {return (idx % 3) == 0})
```

- 元配列 を 変更しない
- return : filter された 新しい 配列


## map

wip:

```
```


### map の return とは

```
wip:
```


## clone

```
ar1 = [0, 1, 2, 3, 4]

ar2 = [...ar1]
```



