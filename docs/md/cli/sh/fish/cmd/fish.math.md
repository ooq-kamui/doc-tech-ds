
# math  -  fish


## cmdline で 計算したいとき

fish の `math` を使いましょう

```
math 1 + 1
```


## 小数点以下の桁数

```
math -s1
```


## file に書いた計算を実行

```txt clc.txt
   1
 + 2
 + 3
```

```
math ( cat clc.txt )
```



