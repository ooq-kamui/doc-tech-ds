
# win11 setup pri


## ctrl2cap install

app installer


## power toys install

win app store ?


## git bash install

app installer


## scoop install

```
set-executionpolicy remotesigned -scope currentuser
```

次のどちらかを実行

```
iex (new-object net.webclient).downloadstring('https://get.scoop.sh')
```

or

```
iwr -useb get.scoop.sh | i
```


## power shell install ( v7, core )

app installer


## fd install

```
scoop install fd
```


## rg install

```
scoop install ripgrep
```


## zoxide install

```
scoop install zoxide
```

or

win-get


## fzf install

```
scoop install fzf
```

## psfzf install

```
Install-Module -Name PSFzf -scope CurrentUser
```

profile.ps1

```
Import-Module PSFzf

Enable-PsFzfAliases
Set-PsFzfOption -PSReadlineChordProvider       'Ctrl+y'
Set-PsFzfOption -PSReadlineChordReverseHistory 'Ctrl+r'
```


## neovim install

```
scoop install neovim
```


## vim-plug install

```
iwr -useb https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim |``
    ni "$(@($env:XDG_DATA_HOME, $env:LOCALAPPDATA)[$null -eq $env:XDG_DATA_HOME])/nvim-data/site/autoload/plug.vim" -Force
```


## neovim plugin fzf-vim install

.vimrc に fzf-vim を記述して install

```
```


## wsl install

```
wsl --install
```


## jq install

- `https://jqlang.github.io/jq/` にアクセス
- `download jq` から `windows ( amd 64 )` を download
  - `jq-windows-amd64.exe` が download される
- 好きな dir ( ~/wrk/app/bin/pwsh/ など ) に置く
- 置いた dir に path を通す


