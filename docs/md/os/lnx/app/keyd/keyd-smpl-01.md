
# sample 01


## ex.1 : capslock を ctrl / esc にする

```
[ids]
*

[main]
# capslock を 押しっぱなし=ctrl, 単押し=esc にする
capslock = overload(control, esc)

# もとの esc を capslock にする ( 不要なら削除 )
esc = capslock
```


## ex.2 : 左 ctrl と capslock を入れ替える

```
[ids]
*

[main]

capslock = leftcontrol
leftcontrol = capslock
```


## ex.3 : レイヤーを使ってシンボル入力を便利にする

```
[ids]
*

[main]
capslock = overload(symbols, esc)

[symbols]
d = ~
f = /
j = (
k = )
l = _
s = -
```


