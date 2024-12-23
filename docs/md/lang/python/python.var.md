
# var


## cp or ref

list ( ary ) は ref



## var scope

### local

とくに記述しなければ local

```
a = 0

def func01():
  a = 1


print(a) # 0
```


### global

```
a = 0

def func01():
  global a
  a = 1

print(a) # 1
```


### block scope

python に block scope はありません



## type の確認

`type()` を使用

```
a = 1
print(type(a))
```


## exists

```
if 'num' in locals():
    print('exists')

```







