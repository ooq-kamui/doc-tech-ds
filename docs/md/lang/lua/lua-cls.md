
# lua class


## basic

```
wip:
```


## : および . の前後は 改行 空白 を挟んでも可

これによって method call の戻り値の object から さらに method call を改行ありでできる

```
$ cat test.lua 
Cls = {
  new = function ()
    local obj = {}
    for key, fnc in pairs(Cls) do
      if key ~= "new" then 
        obj[key] = fnc 
      end
    end
    return obj
  end,

  method1 = function (slf)
    print("method1")
    return slf
  end,

  method2 = function (slf)
    print("method2")
    return slf
  end,
}

Cls.new()
:method1()
:method2()

$ lua test.lua
method1
method2
```


