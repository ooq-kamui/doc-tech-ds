
# syntax


## syntax highlight

group name の確認

調べたい場所に cursor 移動してから

```
:echo synIDattr(synID(line("."), col("."), 1), "name")
```

group name の color の確認

```
:highlight [group name]
```


## syntax highlight setting

syntax file を所定の dir に置く

ex

```
~/.vim/syntax/lua.vim
```


## syntax dir

vim

```
~/.vim/syntax/lua.vim
```

neovim

```
~/.config/nvim/syntax/lua.vim
```

neovim win

```
~/AppData/Local/nvim/syntax/lua.vim
```


## color name list confirm

```
:so $VIMRUNTIME/syntax/colortest.vim
```


## color ref

[color tbl](/vim/color-tbl.html )



