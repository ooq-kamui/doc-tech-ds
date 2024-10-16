
# unix


## sh ch

```
chsh -s /bin/bash
```

https://qiita.com/djkazunoko/items/5f2979e2f902247aac3f


## 環境変数を表示する

```
printenv
```


## N カラム までで sort , 重複数 chk

uniq : 行の比較を最初の N 文字で行う

```
uniq -w N
```

or

```
uniq --check-chars=N
```


## 特定カラムで sort , 重複数 chk

```
wip:
```


## cmdline で計算したいとき

cmdline で計算したいとき, いまは `fish` の `math` でやるのが無難です

```
math 1 + 1
```



