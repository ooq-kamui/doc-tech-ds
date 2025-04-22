
# lua 


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


## 可変長引数の個数

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
$ lua tst002.lua 
3
4
5
6
6
```

うまくすれば method overload ぽいこともできそうだけど,
いまどきはあんまり method overload やらないのかも .. ???

前は 段階的リファクタリングの過程で method overload 使ったりていました


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


## 「local 変数 の 列挙定義」 かつ 「関数戻り値 で 代入」 は 可

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


## 三項演算

```
x = (condition) and val1 or val2
```


## 変数, 引数 の default 値 設定

```
val = val or default_val
```


## 値が nil の配列は pairs() でとばされる

```
> ar = {1,nil,3}
> for idx,val in pairs(ar) do print(idx,val) end
1	1
3	3
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


## 配列を空にする ( 参照している配列は変えずに中身の要素を空にする )

pairs() で回してすべての値に nil を入れる

連想配列と idx 配列が混在しても可

```
> a = {1, 2, a = "a", b = "b", 3, d = "d"}
> for key, val in pairs(a) do print(key, val) end
1 1
2 2
3 3
d d
a a
b b
> for key, val in pairs(a) do a[key] = nil end
> 
> for key, val in pairs(a) do print(key, val) end
> 
> for idx = 1, #a do print(a[idx]) end
>
```

table を二重参照している場合, 一方の変数から テーブルコンストラクタ ( val = {} ) で初期化すると もう一方の変数に反映されないので, これを活用する

```
> a = {1, 2, 3}
> b = a
> a = {}
> print(table.unpack(b))
1 2 3

> a = {1, 2, 3}
> b = a
> for idx, val in pairs(a) do a[idx] = nil end
> print(table.unpack(b))
                  -- &lt;- 空配列
```


## idx 配列の途中に nil を入れても idx が詰まらないので注意

```
> a = {1,2,3}
> a[2] = nil
> table.unpack(a)
1	nil	3
> a = {1,2,3}
> table.remove(a, 2)
2
> table.unpack(a)
1	3
```


## idx 配列で exclude 処理

元配列の参照を変えないで行う

```
$ cat test.lua 
ar = {"a1", "a2", "a3", "a4", "a5", "a6"}
exclude = {"a2", "a4", "a5"}

cnt = 1
idx = 1
while (idx &lt;= #ar) do
  rm = false
  for j, ex in pairs(exclude) do
    if ar[idx] == ex then
      table.remove(ar, idx)
      rm = true
      break
    end
  end
  print(cnt, #ar, table.unpack(ar))
  if not rm then idx = idx + 1 end
  cnt = cnt + 1
end

$ lua test.lua 
1  6  a1  a2  a3  a4  a5  a6
2  5  a1  a3  a4  a5  a6
3  5  a1  a3  a4  a5  a6
4  4  a1  a3  a5  a6
5  3  a1  a3  a6
6  3  a1  a3  a6
```


# 連想配列の要素数は保証されない

```
> ar = {a="a", b="b"}
> #ar
0
```


## 可変長引数 を table に変換

```
val = {...}
```

```
val = table.pack(...)
```


## テーブルコンストラクタの最後の要素が変数列挙のとき 連結される

```
chain = {4 , 5}
val = {1, 2, 3, unpack(chain)}
print(unpack(val))  -- {1, 2, 3, 4, 5}
```

次のようにしても a 配列の中身は 1つしか返っていないので注意

```
> a = {1, 2, 3}
> b = {4, 5, 6}
> c, d, e, f, g, h = table.unpack(a), table.unpack(b)
> print(c, d, e, f, g, h)
1	4	5	6	nil	nil
```

function の引数でも同じ

```
> a = {1, 2, 3}
> b = {4, 5, 6}
> function func(...) print(...) end
> func(table.unpack(a), table.unpack(b))
1  4  5  6
```


## table を変数列挙に変換

```
print(unpack({1, 2, 3}))
```

lua 5.2 以降は table.unpack()

```
print(table.unpack({1,2,3}))
```


## 可変長引数

```
function log(...)
  print(...)
end
```

2個目以降でも可

```
> function a(arg1, ...) print(arg1) print(...) end
> a(1, 2, 3)
1
2	3
```


## 配列の値に nil があると要素数が保証されない

"" , 0 などで初期化が無難

```
> ar = {nil, nil, nil}
> print(#ar)
0
> ar = {"", "", ""}
> print(#ar)
3
> ar = {0, 0, 0}
> print(#ar)
3
```


## 真偽値 ( condition )

nil と false 以外はすべて true

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


## not の解釈で注意

```
if not val1 == val2 then
-- と書くと
-- if (not val1) == (val2) then -- と評価される
-- if not (val1 == val2) then   -- ではないので注意
```


## table のコピー

```
new_tbl = {unpack(org_tbl)}
```


## table へ要素を追加

```
table.insert(t, val)  -- t:table, val:追加する値
```


## table の要素を削除

```
table.remove(t, idx)  -- t:table, idx:index
```


## 小数の切り捨て表示

```
> val = 123.456
> print(string.format("%7.2f", val))
 123.46

-- 7 は . も入れた全体の文字数
-- 小数切り捨てはおおむね四捨五入のようだが厳密でないときもある
```


## 複数行コメントアウト

```
--[[
  コメントアウト部分
--]]
```

コメントアウト部分を実行部分に戻すには
開始側を

```
---[[
```

とするだけで手軽に切り替えられる
終了側を編集する必要はない


## 変数の型を見る

type() を使う

```
print(type(val))  -- val は変数
```


## ランダム値を得る

math.randomseed() をしても最初の math.random() はランダム値にならない  
仕様のようなので1回ダミーで math.random() を実行する  
2回目以降はランダム値が得られます

```
math.randomseed(os.time())
math.random(1,  2) -- dumy, 1回目はランダム値が得られないため
math.random(1, 10) -- 1 - 10 のいずれかの整数を得る
```


## table の内容を出力する (1次配列)

pairs() を使う

```
local tbl = {5,4,3,2,1}
for key, val in pairs(tbl) do
  print(key, val)
end
```

unpack() を使う

```
local tbl = {5,4,3,2,1}
print(unpack(tlb))
```

ただし unpack() は idx 配列にのみ有効

```
> a = {a = "a", b = "b", 3}
> print(table.unpack(a))
3
```

defold であれば pprint() を使ってもよい

```
a = {a = "a", b = "b", c = "c", 1 , 2, 3}
pprint(a)

DEBUG:SCRIPT: 
{
  1 = 1,
  2 = 2,
  3 = 3,
  b = b,
  a = a,
  c = c,
}
```


## 変数名 _ (アンダースコアのみ) も変数として使える

```
> _ = 1
> print(_)
1
```

ダミー変数に使うとよい


## table sort

sort は sort 関数を用いて sort する


