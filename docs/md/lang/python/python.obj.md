
# obj


## key があるか

```
if 'key' in obj:
  print(True)
```


## key は 数字でも ok

```
a = {}

a[123] = 123

print(a)
```

key について, 数値 と 数字の文字列 は区別される

```
a = {}
a[123] = 123
a["123"] = "str123"

print(a)
{123: 123, '123': 'str123'}
```

数値 key の存在チェック は 数値を渡せば ok

```
a = {}
a[123] = 123

123 in a
True

"123" in a
False
```



