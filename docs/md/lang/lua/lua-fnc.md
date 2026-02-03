
# lua fnc


## arg

### arg の default val

```
val = val or val_dflt
```


### 可変長引数

```
function fnc01(...)

  args = {...}

end
```

```
function fnc01(...)

  args = table.pack(...)

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
function a001(...)
  local prm = {...}
  print (#prm)
end

a001("aaa", "bbb", "ccc")
a001("aaa", "bbb", "ccc", "ddd")
a001("aaa", "bbb", "ccc",   nil, "eee") -- 間に nil があってもよさそう
a001("aaa",   nil, "ccc",   nil, "eee", "fff")
a001("aaa",   nil, "ccc",   nil, "eee", "fff", nil) -- 最後が nil だとカウントされない
```

```
3   -- a001("aaa", "bbb", "ccc")                                                             
4   -- a001("aaa", "bbb", "ccc", "ddd")                                                      
5   -- a001("aaa", "bbb", "ccc",   nil, "eee") -- 間に nil があってもよさそう                
6   -- a001("aaa",   nil, "ccc",   nil, "eee", "fff")                                        
6   -- a001("aaa",   nil, "ccc",   nil, "eee", "fff", nil) -- 最後が nil だとカウントされない
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


## return 変数列挙 の function を return 文で call して, 変数列挙ごと受け継ぐ ことは可

```
function a()
  local x, y = 1, 2
  return x, y
end

function b()
  return a()
end

local c1, c2 = b()
print(c1, c2)
```

result

```
1  2
```


## 引数の `(` `)` の省略

- 引数が 1つ で, 文字列 か table constructor の場合は, `(` `)` を省略できる






