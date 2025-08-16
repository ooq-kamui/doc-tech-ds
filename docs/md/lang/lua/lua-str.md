
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


## pad

```
string.format("%03d", i)
```


## sub str

```
string.sub(str, s_idx, e_idx)
```

```
str     文字列
s_idx   切り取り後に 最初の文字となる 元文字列の idx
e_idx   切り取り後に 最後の文字となる 元文字列の idx

idx は lua なので, 1 start
```

ex

1文字取得したい場合, s_idx, e_idx は同じ値

```
string.sub('abcdefg', 3, 3)
```


