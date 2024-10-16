
# vim script


## var ( 変数 )

代入

```
let foo = "hoge"
```

変数の削除

```
unlet foo
```

scope ( var )

```
l : local
a : arg
g : global

b : 現在のバッファ  のローカル
w : 現在のウィンドウのローカル
t : 現在のタブページのローカル
s : vim スクリプトのローカル
v : グローバル, vimの定義
```


## loop

### for

```
for val in range(1, 9)

  echo val

endfor
```

```
for val in [1, 2, 3]

  echo val

endfor
```

### while

break も使える

```
while <cnd>

  if <cnd>
    break
  endif

endwhile
```

continue も使える


do while はありません ( たぶん )



## 文字列

```
"" : desc
'' : desc
```

### 文字列 連結

```
let str = 'vim'
echo 'this editor is ' . str . ' !'
```


## comment

```
" comment
```


## function arg

```
a:0    引数の数
a:n    n番目の引数
a:000  すべての引数の配列
```


## func lib

```
https://vim-jp.org/vimdoc-ja/usr_41.html#function-list
```


## normal コマンドを実行

```
normal cmd_str
```



