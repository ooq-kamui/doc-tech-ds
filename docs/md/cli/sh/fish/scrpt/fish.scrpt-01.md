
# fish script


## 真偽値

```
true  : 0
false : 1
```


## stdin を 変数 に読み込む 

```
set list read
```


## 直前の command の status

```
$status
```

```
0         success
それ以外  err
```

ex

```
echo $status
```

ref
https://natsukium.github.io/fish-docs-jp/tutorial/exit_status.html



