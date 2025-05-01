
# lua var


## bool

```
a = true
```

```
b = false
```


### nil と false 以外はすべて true

```
if nil then
  print("true")
else
  print("false")
end
```

```
false
```

```
if false then
  print("true")
else
  print("false")
end
```

```
false
```

```
if 0 then
  print("true")
else
  print("false")
end
```

```
true
```

```
if "" then
  print("true")
else
  print("false")
end
```

```
true
```


## var type

type() を使う

```
print(type(val))
```


## nil と false を区別したい場合は type() を見る

```
a = nil
if not a and type(a) == "nil" then
  print("a = nil")
end
```

```
a = nil
```

```
a = false
if not a and type(a) == "boolean" then
  print("a = false")
end
```

```
a = false
```


## local 変数 の 列挙定義 かつ 関数戻り値 で 代入 は 可

```
$ cat test001.lua 
function fnc1()

  local val1, val2 = fnc2()

  print(val1, val2)

  return val1, val2
end

function fnc2()
  return 88, 99
end

local a, b = fnc1()
print(a, b)

$ lua test001.lua 
88	99
88	99
```


## 変数名 _ (アンダースコアのみ) も変数として使える

```
> _ = 1
> print(_)
1
```

ダミー変数に使うとよい


