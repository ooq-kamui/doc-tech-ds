
# sample 02

- keyd で定番のパターン


## 1. capsLock を ctrl / esc に ( 最も人気 )

tap で esc, 長押しで ctrl になるいわゆる "Dual-role CapsLock"

```
[ids]
*

[main]
capslock = overload(control, esc)
# esc を capslock に swap
esc = capslock
```


## 2. space を修飾キーに ( space cadet / space-layer )

- tap で space, hold で layer 
- home position から arrow key を使えるように

```
[main]
space = overload(nav, space)

[nav]
h = left
j = down
k = up
l = right
u = pageup
d = pagedown
```


## 3. home row mods

home position の key ( a, s, d, f / j, k, l, ; ) を,  
tap/hold で 修飾キーにする

```
[main]
a = overload(meta, a)
s = overload(alt, s)
d = overload(shift, d)
f = overload(control, f)

j = overload(control, j)
k = overload(shift, k)
l = overload(alt, l)
; = overload(meta, ;)
```

QMK 界隈で流行している設定を keyd で再現したもの  
誤爆が気になる場合は `overloadt()` (timeout 付き) や `overloadt2()` で閾値を調整できる


## 4. oneshot modifier

- 1 回だけ次のキーに修飾をかける
- sticky keys に近い概念

```
[main]
leftshift = oneshot(shift)
leftcontrol = oneshot(control)
```


## 5. macOS 風 short-cut ( super を ctrl 代わりに )

linux に移行した macOS ユーザーがよくやるパターン

```
[main]
leftmeta = layer(mac)

[mac]
c = C-c
v = C-v
x = C-x
a = C-a
z = C-z
s = C-s
w = C-w
t = C-t
q = C-q
f = C-f
```


## 6. 右 alt ( AltGr ) でレイヤーを作り記号を打ちやすくする

```
[main]
rightalt = layer(symbols)

[symbols]
j = (
k = )
u = [
i = ]
m = {
, = }
```

- 数字列まで指を伸ばさずに括弧を打てる
- プログラマー向け


