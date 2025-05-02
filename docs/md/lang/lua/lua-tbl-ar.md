
# table


## ar

```
ar = {
  'aa',
  'bb',
}
```


## len

```
tbl = {0, 1, 2}

print(#tbl)
```


### 配列の値に nil があると要素数が保証されない

"" , 0 などで初期化が無難

```
ar = {nil, nil, nil}
print(#ar)
```

```
0
```

```
ar = {"", "", ""}
print(#ar)
```

```
3
```

```
ar = {0, 0, 0}
print(#ar)
```

```
3
```


## table の cp

```
new_tbl = {unpack(org_tbl)}
```


## table add

```
table.insert(t, val)  -- t:table, val:追加する値
```


## table del

```
table.remove(t, idx)  -- t:table, idx:index
```


## 配列 の中の nil は pairs() で とばされる

```
ar = {1, nil, 3}

for idx, val in pairs(ar) do
  print(idx, val)
end

1	1
3	3
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


## table sort

sort は sort 関数を用いて sort する


