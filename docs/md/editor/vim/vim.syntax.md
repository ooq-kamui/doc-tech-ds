
# syntax highlight


## group name の確認

調べたい場所に cursor 移動して

```
:echo synIDattr(synID(line("."), col("."), 1), "name")
```

group name の color の確認

```
:highlight [group name]
```


## setting

syntax file を所定の dir に置く

### vim

```
~/.vim/syntax/lua.vim
```

### neovim

```
~/.config/nvim/syntax/lua.vim
```

### neovim win

```
~/AppData/Local/nvim/syntax/lua.vim
```


## color name list confirm

```
:so $VIMRUNTIME/syntax/colortest.vim
```


## color ref

[color tbl](https://www.ooq.jp/tech/ds/vim/color-tbl.html )



