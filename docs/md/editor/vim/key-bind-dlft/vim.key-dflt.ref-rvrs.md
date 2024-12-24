
# 逆引き - 基本機能 ( やりたいことから )


## cursor mv

単語移動

```
e   単語の末尾に進む
w   単語の先頭に進む
W   単語の先頭に進む
E   単語の末尾に進む

b   単語の先頭に戻る
ge  単語の末尾に戻る
B   単語の先頭に戻る
gE  単語の末尾に戻る
```


行番号を指定して移動

```
:行番号
```


cursor pos を画面中央に

```
zz
```


## search


search - 検索

```
/str
```

search cursor pos word

```
*
```

word search

```
/<word>
```


## replace 置換

replace  -  確認しながら

```
:%s/str/rpl/gc
```

replace repeat  -  置換を繰り返す

```
:s
```

で 最後の置換を実行


検索文字を置換

```
/str
```

を一度実行し 検索レジスタに文字がある状態にする

```
:%s//rpl/g
```


置換後文字列中に改行

```
ctl-v <cr>
```

文字置換

```
r
```


## 連番

visual mode で選択

```
g<c-a>
```


## sort

sort , 昇順

```
:sort
```

sort , 逆順

```
:sort!
```


## 逆順 ( sort しない単なる逆順 )

```
:'<,'>!tail -r
```


## edit

str upper

```
( visual mode )
U
```

str lower

```
( visual mode )
u
```

str upper / lower

```
( visual mode )
~
```


## del

del line - 1行削除

```
dd
```

del word - 1単語削除

```
dw
```

行の文字を削除

```
0D
```

カーソル行から最後の行まで削除

```
dG
```

カーソル行から最後の行まで削除

```
VGd
```

全行削除


## insert, add

行末に文字追加

```
A     ... a
```

複数行の行末に文字追加

```
ctl-v
j などで行選択
$
A
```


yank line all - 全行をヤンク

```
:%y
```


## select

select word - 単語選択

```
viw   ... Viw ???
```


## select box

select box  - 矩形選択

```
ctl-v
```

select box insert

```
ctl-v
jlなどで select
I
inputstr
<esc>
```

select box add $

```
ctl-v
jなどで select
$A
inputstring
<esc>
```

select box yank

```
ctl-v
jlなどで select
y
```

select box cut

```
ctl-v
j l などで select
x
```

visual line に対して 置換

```
:'<,'>s/str/rpl/gc
```

visual box  に対して 置換

```
:'<,'>:s/\%Vhoge/foo/gc
```

undo

```
u
```

redo

```
ctl-r
```

redo line

```
U
```


## indent

indent down

```
visual line mode で行選択
>
```

indent up

```
visual line mode で行選択
<
```

indent tab > space

```
:1,$!expand -2

:set expandtab
:retab x
```

indent space > tab

```
:set noexpandtab
:retab! x
```


## tab

sh から tab で開く

```
$ vim -p *.txt
```

tab で開く

```
:tab    [filename]
:tabnew [filename]
```

次の tab

```
gt
```

前の tab

```
gT
```


## tab順 移動

1番目に移動

```
:tabm 0
```

最後に移動

```
:tabm
```

右に移動

```
:tabm +1
```

左に移動

```
:tabm -1
```


## tag jump  -  cursor 上の file path を新しい tab で開く

行番号なし

```
ctl-w gf
```

行番号あり

```
ctl-w gF
```


## split  -  画面分割

split - 水平

```
:split
```

split - 垂直

```
:vsplit
```

```
:vs
```

split 終了

```
ctl-w c
```


## window cursor mv

window mv l - 左

```
ctl-w h
```

window mv r - 右

```
ctl-w l
```

window mv u - 上

```
ctl-w k
```

window mv d - 下

```
ctl-w j
```

window mv 次

```
ctl-w w
```


## window pos mv

window pos mv 左

```
ctl-w H
```

window pos mv 下

```
ctl-w J
```

window pos mv 上

```
ctl-w K
```

window pos mv 右

```
ctl-w L
```

window pos mv 回転

```
ctl-w r
```


## window size

window width 増

```
ctl-w >
```

window width 減

```
ctl-w <
```

window height 増

```
ctl-w +
```

window height 減

```
ctl-w -
```

window close other

```
:only
```



