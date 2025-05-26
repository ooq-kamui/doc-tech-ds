
# tbl obj


## basic

```
obj = {
  a = 'aa',
  b = 'bb',
}
```

`.` つなぎから 新規代入 可

```
obj = {}

obj.c = 1
```

table constructor では key の str を quote すると err

```
-- err

obj = {
  'a' = 1
}
```

key に使える 文字

添字記法 なら, 記号も わりといけます

```
a = {}

a['a+a'] = 1
a['a-a'] = 1
a['a=a'] = 1
a['a#a'] = 1
```

すべては未確認


## 連想配列の要素数は保証されない

```
ar = {a="a", b="b"}
#ar
```

```
0
```


## 連想配列の要素の削除

連想配列の値に nil を代入することは その変数(要素)を削除することと同等なのでこれを利用する

```
> a = {a = "a", b = "b", c = "c"}
> for key, val in pairs(a) do print(key, val) end
a a
b b
c c

> a.b = nil
> for key, val in pairs(a) do print(key, val) end
a a
c c

> -- そもそも 存在しない key を参照しようとしても
> -- nil が返るのみでエラーとはならない
> print(a.d)
nil

> -- なので, 値に nil を入れると, 
> -- それまでに宣言されていない変数と挙動が同等となる

> -- また key 名を明示的に指定しない参照は
> -- pairs() ぐらいしかない (と思われる, 素直な作りであれば) 
> -- pairs() は値が nil　の場合には処理をとばすので, 
> -- その key がないのと挙動が同等となる


> -- 注) idx 配列の要素数や unpack() では nil 値でもとばされません
> b = {"a", nil, "c"}
> print(#b)
3
> table.unpack(b)
a nil c
```


