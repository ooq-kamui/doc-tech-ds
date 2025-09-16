
# nvim lua


## ref

https://github.com/willelz/nvim-lua-guide-ja/blob/master/README.ja.md

https://lab.mo-t.com/blog/neovim-v05-introduction-new-features-part-1


## init.lua

- init.vim と同じ dir に置く
- init.vim と init.lua を両方読み込むことはできない
  - どちらか 1つ に 決める必要がある

### linux

```
~/.config/nvim/init.lua
```

### win

```
$HOME/AppData/local/nvim/init.lua
```


## lua file dir

### linux

```
~/.config/nvim/lua
```

### win

```
$HOME/AppData/local/nvim/lua
```


## require

```
require('tst')
```

file location

```
~/.config/nvim/lua/tst.lua
```

- require() では 再読み込みできない
- とはいえ, ひとまず, require() で読み込んでおくのが無難


## `_G`

```
_G :  lua がわ vim script 側 共通の global 名前空間
      function を 呼べる
        vim script 側
          call _G.My_fnc()
```


## plugin

ref

https://zenn.dev/vim_jp/articles/20231113vim_ekiden


## print / echo / log

```
print(val)
```

のあと

```
:message
```

する必要がある


