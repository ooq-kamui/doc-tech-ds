
# sample 02

keyd で定番とされる設定パターンをまとめます


## 1. CapsLock を Ctrl / Esc に (最も人気)

tap で Escape, 長押しで Control になるいわゆる "Dual-role CapsLock"

```
[ids]
*

[main]
capslock = overload(control, esc)
# esc を capslock に swap
esc = capslock
```

Vim ユーザーにも Emacs ユーザーにも恩恵がある, keyd README にも Quickstart として載っている鉄板設定です


## 2. Space を修飾キーに (Space Cadet / Space-layer)

tap で Space, 長押しでカスタムレイヤーに入る

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

ホームポジションから矢印キーを使えるようになる


## 3. Home Row Mods

ホームロー (a, s, d, f / j, k, l, ;) を tap/hold で修飾キーにする

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


## 4. oneshot modifier (ワンショット)

1 回だけ次のキーに修飾を掛ける. Sticky Keys に近い概念

```
[main]
leftshift = oneshot(shift)
leftcontrol = oneshot(control)
```

連続入力のとき指を押さえ続けなくてよくなる


## 5. macOS 風ショートカット (Super を Ctrl 代わりに)

Linux に移行した macOS ユーザーがよくやるパターン

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


## 6. 右 Alt (AltGr) でレイヤーを作り記号を打ちやすくする

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

プログラマー向け. 数字列まで指を伸ばさずに括弧を打てる


