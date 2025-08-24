
# lua loop


## for 文

```
for idx = 1, 10 do

  print(idx)
end
```

```
local tbl = {1, 2}

for idx, val in pairs(tbl) do

  print(idx, val)
end
```


## while 文

```
while #a > 0 do

  print(#a) 
  table.remove(a) 
end
```

```
local idx = 10

while idx > 0 do

  print(idx)

  idx = idx - 1
end
```


## repeat ( do while )

```
local idx = 1

repeat

  print(idx)

  idx = idx + 1

until idx > 10
```

- until の true / false が直感に反するので注意
- while から repeat に作り変えた場合, true / false を逆にする必要がある  
  ( not をつける )


## continue

lua に continue はありません


## for 文の idx, val は for 内での local 変数になる

```
$ cat tst001.lua 
function test()

	local ar = {1,2,3,4,5}

	local idx = 200
	local val

	for idx, val in pairs(ar) do
		print(idx)
	end
	print(idx, val)
end

test()
print(idx)

$ lua tst001.lua
1
2
3
4
5
200	nil
nil
```


## 配列 を for ループ中に その配列の要素を table.remove() するときの注意

idx increment と in pairs() の違い

```
> a = {"a", "b", "c"}
> for i = 1, #a do 
>> print(i, a[i])
>> table.remove(a)
>> end
1 a
2 b
3 nil
-- 最初の要素数分ループする
-- つまり #a を初回評価するのみ (と思われる) 
```

```
> a = {"a", "b", "c"} 
> for i, val in pairs(a) do 
>> print(i, val)
>> table.remove(a)
>> end
1 a
2 b
-- 最初の要素数分ループしない
```

ケースによっては nil 代入による削除で行ってもよい
連想配列の要素の削除 の項 も参照

nil 代入による削除 は idx 配列でも可能

ちなみに while では #a が都度評価される

```
a = {1,2,3}
> while #a > 0 do 
>> print(#a) 
>> table.remove(a) 
>> end
3
2
1
```


