
# string  文字列  -  fish


## replace  置換

```
string replace "srch" "rpl" "target"
```


## split  分割

```
string split ' '  $lst
```

notice : tab を分割することはできないかも ?

事前に tab を space に変換しておいて, space の 分割にするのが better
( たぶん )


## str の 単純な 連結

```
wip:
```


## join ( str lst の 連結 )

```
string join , $lst
```


## here document

```
string trim '
a
b
'

? wip:
```



## match

ex

```
string match -r '[^.]+$' $argv[1]
```


### ext  拡張子  -  match

```
string match -r '[^.]+$' $argv[1]
```


## trim

```
string trim '    apple    '
```

### option

```
-l   : 左側のみ trim
-r   : 右側のみ trim

-c   : 任意文字の trim
```

### 任意文字の trim

```
string trim -c '#' '###aaabbbccc###'
```


