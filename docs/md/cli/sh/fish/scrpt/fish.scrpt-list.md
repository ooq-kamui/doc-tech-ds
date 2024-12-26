
# fish script list


## list の定義 ( 代入 )

```
set lst aaa bbb ccc
```


### 1行 に 1要素, ヒアドキュメントのように 定義したい場合

改行を無視を活用

```
set lst \
  a     \
  b     \
  c     \

for $i in $lst
  echo $i
end
```


## list の count ( 要素数 )

```
count $argv
```


## list に add ( 配列 に 追加 )

```
set lst $lst aaa
```


## 削除

```
wip:  ないかも?
```


## list に val があるか ( in_ar )

```
contains
```

ex

```
set lst aaa bbb ccc

if contains $argv[1] $lst
    echo "true"
end
```



