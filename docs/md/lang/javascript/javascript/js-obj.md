
# object


## key add

```
a = {}
a.a = 'a'

a['b'] = 'b'
```


## プロパティがあるか

```
obj.hasOwnProperty('prp_name')
```

```
if ('prp_name' in obj){

}
```


## obj clone & 特定 key のみ値の変更 を, spread syntax & 代入 でやる

```
prv = {a: 1, b: 2, c: 3}

obj = {...prv, b: 22}
```


## optional chaining

```
const key01 = obj?.key01
```

- obj が undefined でも error にならずに key01 は undefined になる



