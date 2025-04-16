
# vimdiff


## cursor mv win

```
ctl-w l : mv r
ctl-w h : mv l
```


## merge

```
差分箇所で dp  cursor のあるほうの内容を もう一方のファイルに反映
差分箇所で do  cursor のないほうの内容を もう一方のファイルに反映

dp : diff put
do : diff obtain
```


## color

vimdiff の color setting

```
highlight DiffAdd    ctermfg=10 ctermbg=22 cterm=none
highlight DiffDelete ctermfg=10 ctermbg=52 cterm=none
highlight DiffChange ctermfg=10 ctermbg=17 cterm=none
highlight DiffText   ctermfg=10 ctermbg=21 cterm=none
```


## design

```
wip: ??
```



