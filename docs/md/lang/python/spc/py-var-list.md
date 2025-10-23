
# list


## 要素数

```
a = [1, 2, 3]

cnt = len(a)
```


## add  -  1要素 を追加

```
list01 = []

list01.append('a')
```


## list の末尾に 別の list を連結 ( 結合 )

```
a = [1, 2, 3]
b = [4, 5, 6]

a.extends(b)
```


## 値があるか ( in array )

```
x = 'a'

if x in ['a', 'b']:
  print('true')
```


## 2次元 list の n 番目の要素を 1次元 list として取得

```
a = [
  ['a1', 'b1'],
  ['a2', 'b2'],
  ['a3', 'b3'],
]
b = [sub_list[0] for sub_list in a]
print(b)
```


## list のすべての要素が empty ( None or '' )

```
wip:
```




