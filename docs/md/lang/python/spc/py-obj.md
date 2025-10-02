
# obj


## def

```
obj = {
  "key01": "val01",
  "1"    : "1",
  1      : 1,
}
```


## 代入

```
obj = {}
obj['b'] = 2

# obj.a = 1   # これは ng ( py では できない )
```


## key があるか

```
if 'key' in obj:
  print(True)
```


## obj の key があれば取り出し, なければ 指定値

```
obj = {}
obj['a'] = 'a1'
obj['b'] = 'b1'

c = obj.get('c', 'c1')
```


## key は 数字でも ok

```
a = {}

a[123] = 123

print(a)
```

### key について, 数値 と 数字の文字列 は区別される

```
a = {}
a[123] = 123
a["123"] = "str123"

print(a)
{123: 123, '123': 'str123'}
```

### 数値 key の存在チェック は 数値を渡せば ok

```
a = {}
a[123] = 123

123 in a
True

"123" in a
False
```

## unpack

```
*   : key の unpack
**  : val の unpack
        key と val の unpack ?
```

key の unpack なんてほとんど使わない ?


