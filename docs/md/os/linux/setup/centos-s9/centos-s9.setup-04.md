
# centos stream 9  -  env setup part 04  -  ( sakura vps )


## fd

```
brew install fd
```


## rg

```
brew install rg
```


## fzf

```
brew install fzf
```


## vim-plug

```
sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs \
       https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
```


## fzf.vim

vim から

```
:PlugInstall
```


## vim syntax

```
cd ~/.local/share/nvim/site

ln -s ~/wrk/cnf/vim/cnf/syntax .
```


## fish color

ex

`config.fish`

```
set fish_color_command syan
```



