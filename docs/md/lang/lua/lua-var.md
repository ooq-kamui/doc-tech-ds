
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
> if nil then print("true") else print("false") end
false
> if false then print("true") else print("false") end
false
> if 0 then print("true") else print("false") end
true
> if "" then print("true") else print("false") end
true
```


## nil と false を区別したい場合は type() を見る

```
> a = nil
> if not a and type(a) == "nil" then print("a = nil") end
a = nil

> a = false
> if not a and type(a) == "boolean" then print("a = false") end
a = false
```


