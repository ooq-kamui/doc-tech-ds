
# vim  -  set


## 文字コードの自動判定

```
set encoding=utf-8
set fileencodings=utf-8,sjis
```


## マウス の クリックを無効 ( ホイールは有効 )

```
set mouse=n
map <LeftMouse> <Nop>
```


## vim を閉じても undo 継続

```
mkdir ~/.vim-undo
```

`.vimrc`

```
if has('persistent_undo')
  set undodir=~/.vim-undo
  set undofile                                                                                                                                   
endif
```


