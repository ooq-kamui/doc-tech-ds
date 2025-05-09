
# win11 setup ofc


## ctrl2cap

installer

```
ctrl2cap.exe /install
```


## git

git for windows installer

`.gitconfig`
- cp fr old


## power toys

installer


## power shell ( v7 )

installer


## windows terminal

installed pre


## scoop

install

```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

```
Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
```

path add ??

profile_env.ps1

```
$ENV:Path += ";$home\scoop\shims"
```


## zoxide

```
scoop install zoxide
```


## rg

```
scoop install ripgrep
```

- `.ripgreprc` は profile で設定されている


## fd

```
scoop install fd
```


## fzf

```
scoop install fzf
```

psfzf

```
Install-Module -Name PSFzf -scope CurrentUser
```


## neovim

```
scoop install neovim
```

init.vim

- cp fr old

ln

```
New-Item -ItemType SymbolicLink -Path lua -Value C:\Users\xxx\wrk\prj-pri\dotfiles\nvim\scrpt\dflt\lua
```

```
New-Item -ItemType SymbolicLink -Path syntax -Value C:\Users\xxx\wrk\prj-pri\dotfiles\nvim\syntax\pwsh
```

vim-plug

```
iwr -useb https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim |`
    ni "$(@($env:XDG_DATA_HOME, $env:LOCALAPPDATA)[$null -eq $env:XDG_DATA_HOME])/nvim-data/site/autoload/plug.vim" -Force
```

```
:PlugInstall
```


## neovim-qt

```
wip:
```


## node

installer

win-term から restart  
( 同 win-term で 新 pwsh 起動 では認識されない )


