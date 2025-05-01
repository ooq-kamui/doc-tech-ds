
# fnc


## basic

```
wip:
```


## arg

### arg の default val

```
val = val or default_val
```


### 可変長引数

```
function fnc01(...)

  val01 = {...}

  val02 = table.pack(...)
end
```

2個目以降でも可

```
function fnc02(arg1, ...)

  print(arg1)
  print(...)
end

fnc02(1, 2, 3)
```

```
1
2	3
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


## table コンストラクタ内で直接 function を定義することも可

```
$ cat test.lua 
fnc_ar = {
  function ()
    print("fnc1")
  end,
  function ()
    print("fnc2")
  end,
}

fnc_ar[1]()
fnc_ar[2]()

$ lua test.lua 
fnc1
fnc2
```


## return 変数列挙 の function を return 文で call して, 変数列挙ごと受継ぐことは可

```
$ cat tst.lua
function a()
  local x, y = 1, 2
  return x, y
end

function b()
  return a()
end

local c1, c2 = b()
print(c1, c2)

$ lua tst.lua
1  2
```


