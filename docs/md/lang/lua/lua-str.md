
# lua str


## 連結

```
str03 = str01 .. str02
```


## escape

escape 文字は `\`

```
-- '' の文字列でも, "" の文字列でも 共通

'aaa\'bbb'

"aaa\"bbb"
```


## find ( srch idx )

str の中から, ptn の 一致する s_idx, e_idx を返す

```
s_idx, e_idx = string.find('abcdefg', 'cd', srch_s_idx)
```

ex

```
s_idx, e_idx = string.find('abcdefg', 'cd')
print(s_idx, e_idx) -- 3, 4
```


## 文字列の分割

```
> s = "hello world from Lua"
> for w in s:gmatch("%a+") do
>>   print(w)
>> end
hello
world
from
Lua
```


## ゼロパディング

```
string.format("%03d", i)
```


## sub string

```
string.sub(str, idx_s, idx_e)
```

```
str     文字列
idx_s   切り取り後に 最初の文字となる 元文字列の idx
idx_e   切り取り後に 最後の文字となる 元文字列の idx

idx は lua なので, 1 start
```

ex

1文字取得したい場合, idx_s, idx_e は同じ値

```
string.sub('abcdefg', 3, 3)
```


