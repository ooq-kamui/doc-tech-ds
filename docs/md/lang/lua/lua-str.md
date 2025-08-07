
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


