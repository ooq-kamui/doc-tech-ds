
# vim


## .vimrc reload

```
:source ~/.vimrc
```


## .vimrc path を確認

```
:echo $VIM
```


## cmd line から複数ファイル を tab で起動

```
vim -p **/memo.*.md
```


## neovim の ver up

ver 確認

```
nvim -v
```

### brew の場合

brew の update

```
brew update
```

brew で neovim の verup

```
brew upgrade neovim
```


## open file

```
:e [file_name]
```


## 標準入力 を vim で開く

```
cat filename | vim -
```

## quit all

```
:qa
```


## wrap ( 行の折り返し )

行を折り返す

```
:set wrap
```

行を折り返さない

```
:set nowrap
```


## mac の vim で tab を入力する

insert mode で

```
ctl-v
<tab>
```


## visual line にのみコマンドを実行

V などで選択後

: を入力すると

```
:'<,'>
```

と表示されるので, 続けて コマンドを入力すればよい

ex

```
:'<,'>!pwd
```

結果が 選択していた範囲に insert される

もとの行は delete されます


## sort

```
:sort
```

sort desc

```
:sort!
```


## mark

mark lst を表示

```
:marks
```

mark を つける

```
:mark a
:ma a
:k a   < ?
```

mark を 削除

```
:delmark a
```

mark を 削除 all

```
:delmark!
```

mark へ jmp

```
`a 
'a 
```

mark へ jmp 検索

```
[`
]`
['
]'
```


## 検索?

```
yank した文字列を置換
yank した文字列で置換
yank した文字列で検索
```

## カーソル位置の単語で検索

```
*
```


## grep

sub dir も対象

```
:grep ptrn **.lua
```

2種類の file type を対象

```
:grep ptrn **.lua **.script
```

すべての sub dir file を対象

```
:grep ptrn **
```

1つ目の file を自動的に開かない

```
:grep! ptrn **.lua
```

編集中の file を対象

```
:grep ptrn %
```

grep 結果を tab で開く

```
autocmd QuickFixCmdPost vimgrep,grep tab cwindow
```


## quickfix

quickfix を filter する

```
:packadd Cfilter
:Cfilter ptrn
```


## vimgrep

大文字小文字の区別

```
/\c    " 大文字小文字を区別しない
```

```
/\C    " 大文字小文字を区別する
```


## colorscheme

```
:colorscheme [colorscheme]
```


## highlight

highlight color confirm

```
:highlight
```


## c tags

tags file の確認

```
:echo tagfiles()
```

tags file cre

```
ctags -R --languages=lua -f .tags
```


## vim script

script 内で normal コマンドを実行

```
:normal cmd
```


## key bind の確認

自分で割り当てた key bind の確認

```
:map           " mode all
:imap          " mode insert
:nmap          " mode nomal
:vmap          " mode visual
:verbose nmap  " 定義元ファイル情報も表示
```


## mode ins から esc のタイムラグを消去

tmux で

```
set -s escape-time 0
```


## netrw ( filer )

```
:Ex
```

```
:e .
```



