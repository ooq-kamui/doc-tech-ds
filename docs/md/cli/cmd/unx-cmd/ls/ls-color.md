
# ls  color


# color

## mac

```
wip:
```


## linux

### setting

現在の color setting を取得

```
dircolors -p > ~/.colorrc
```

`.colorrc` の color setting を変更

`.colorrc`

```
# :
# :

RESET 0 # reset to "normal" color
DIR 01;35 # directory
LINK 01;36 # symbolic link. (If you set this to 'target' instead of a
# numerical value, the color is as for the file pointed to.)

# :
# :
```

`~/.colorrc` を `~/.bashrc` に設定

`.bashrc`

```
eval `dircolors ~/.colorrc`

# alias ls='ls --color=auto'
```

bash で login してから fish に切り替えている場合,
上記で fish にも反映される


### color code

```
30  black
31  red
32  green
33  yellow
34  blue
35  purple
36  cyan
37  white
```


### ref

https://qiita.com/PinkPhayate/items/a670e7e7935baea988f2

https://www.gfd-dennou.org/arch/morikawa/memo/ls_colors.txt


