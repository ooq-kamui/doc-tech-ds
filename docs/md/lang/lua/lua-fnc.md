
# fnc


## basic

```
wip:
```


## arg

### 可変長引数

```
function log(...)
  print(...)
end
```

2個目以降でも可

```
function a(arg1, ...)

  print(arg1)
  print(...)
end
```

```
a(1, 2, 3)
1
2	3
```


### 可変長引数 を table に変換

```
val = {...}
```

```
val = table.pack(...)
```


### 可変長引数の個数

```
$ cat tst001.lua
function a001(...)
  local prm = {...}
  print (#prm)
end

a001("aaa", "bbb", "ccc")
a001("aaa", "bbb", "ccc", "ddd")
a001("aaa", "bbb", "ccc",   nil, "eee") -- 間に nil があってもよさそう
a001("aaa",   nil, "ccc",   nil, "eee", "fff")
a001("aaa",   nil, "ccc",   nil, "eee", "fff", nil) -- 最後が nil だとカウントされない

$ lua tst001.lua 
3
4
5
6
6
```


