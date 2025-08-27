
# fish script


## var

```
set var01 val01
```


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


## 実行している script の file name

### file-name

```
set script_file_name ( status filename )
```

### file-path ( abs )

file-path ( abs ) は直接取れないので, readlink を活用する

```
set script_file_name ( status filename )
set script_file_path ( readlink -f $script_file_name )
```

### dir-rel

```
set dir_rel ( status dirname )
```

### dir-abs

dir ( abs ) は直接取れないので, readlink を活用する

```
set dir_rel ( status dirname )
set dir_abs ( readlink -f $dir_rel )
```


## ref

https://natsukium.github.io/fish-docs-jp/tutorial/exit_status.html


