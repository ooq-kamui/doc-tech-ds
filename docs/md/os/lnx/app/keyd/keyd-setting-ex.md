


### ex.1 : CapsLock を Ctrl / Esc にする ( 定番 )

押しっぱなし -> Ctrl, 単押し -> Esc

```ini
[ids]
*


[main]
# CapsLock を 押しっぱなし=Ctrl, 単押し=Esc にする
capslock = overload(control, esc)


# 元の Esc を CapsLock にする ( 不要なら削除 )
esc = capslock
```


### ex.2 : 左 Ctrl と CapsLock を入れ替える ( シンプル )

```ini
[ids]

*

[main]

capslock = leftcontrol
leftcontrol = capslock
```


### ex.3 : レイヤーを使ってシンボル入力を便利にする

```ini
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


