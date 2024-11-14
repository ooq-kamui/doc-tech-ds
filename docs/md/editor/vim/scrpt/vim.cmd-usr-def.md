
# vim cmd  -  usr def

ref

https://vim-jp.org/vimdoc-ja/usr_40.html


## arg

上記のページには, `<f-args>` `<q-args>` が cmdline 上でどう展開されるかの説明のされている

しかし, そこは cmd 定義者 がもあまり気にしても意味のないところで,
要は, 次のように func に arg が渡される


### `<f-args>`

#### desc

- cmd で 複数 arg は, func には 複数 arg として 渡される
- 文字列は およそそのまま 渡される

#### ex

```
command! -bang -nargs=* TstArgF call Tst_arg_f(<f-args>)

func! Tst_arg_f(arg01, arg02, arg03, arg04) range abort

  echo a:arg01
  echo a:arg02
  echo a:arg03
  echo a:arg04
endfunc
```

```
:TstArgF aa().a \/|&bbb 'aa().a \/|&bbb'
```

```
aa().a
\/|&bbb
'aa().a
\/|&bbb'
```


### `<q-args>`

#### desc

- cmd で 複数 arg は, func には 1 つ の arg として渡される
- 文字列は およそそのまま 渡される
- cmd で arg がない場合は, func には 空文字列 が渡される

#### ex

```
command! -bang -nargs=* TstArgQ call Tst_arg_q(<q-args>)

func! Tst_arg_q(arg01) range abort

  echo a:arg01
  " echo a:arg01 . 'end'
endfunc
```

```
:TstArgQ aa "bbb ccc" '().\a bbb""' "().\a bbb''"
```

```
aa "bbb ccc" '().\a bbb""' "().\a bbb''"
```


### `<args>`

#### desc

- 与えられた通りのコマンド引数

#### ex

wip:



