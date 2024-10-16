
# while read


## 標準入力を行ごとに処理する

```
cat a.txt | while read line
do
  echo $line
done
```

1行で書く場合

```
cat a.txt | while read line ;do echo $line ; done
```



