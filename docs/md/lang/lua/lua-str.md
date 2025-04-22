
# lua str


## escape

escape 文字は `/`

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





