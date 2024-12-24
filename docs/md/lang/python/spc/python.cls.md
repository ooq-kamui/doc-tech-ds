
# class


## ref

https://docs.python.org/ja/3/tutorial/classes.html


## class def

```
class MyClass:

    # method def ...

```

```
obj = MyClass()
```


## constructor

```
class MyClass:

    def __init__(self):
        self.data = []
```


## method

```
class MyClass:

    def method01(self):
        self.data = []
```


## property ( object )

他の言語で property, field などと呼ばれる 変数 を
python では オブジェクト と呼んでいるらしき

```
class MyClass:

    def method02(self):
        self.a = 1
        self.b = 2
        return

    def method02(self):
        return self.b
```



