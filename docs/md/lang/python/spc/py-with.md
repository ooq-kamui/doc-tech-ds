
# with


## python の with とは ?

with を使うと, 後処理を自動的にやってくれる,
ということのようである


### with 使用 の場合

```
with open('test.txt', 'r') as file:
  print(file.read())
```


### with 使用しない場合

```
file=open('test.txt','r')
text=file.read()
print(text)
file.close()
```

のように書く必要がある



