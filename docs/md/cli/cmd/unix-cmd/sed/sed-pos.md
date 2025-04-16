
# 位置指定


## 最後の行

```
sed "$ s/find/rpl/g"
```


## m 行目 から n 行目

```
sed "m,n s/find/rpl/g"
```


## m 行 のみ

```
sed "m s/srch/rpl/g"
```


## key のある行

```
sed "/key/ s/find/rpl/g"
```


## key1 のある行 から key2 のある行

```
sed "/key1/,/key2/ s/find/rpl/g"
```


## 複数条件 ( 複合 )

```
wip:
```


