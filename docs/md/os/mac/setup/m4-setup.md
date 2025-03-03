
# mac m4  -  setup


## karabiner

install by installer

config file fr m1

fn key setting

```
wip:
```


## terminal

### profile

import fr m1 export


## brew

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

```
echo >> /Users/kamui/.zprofile
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> /Users/kamui/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
```


## git

brew を install すると
git  も install される


## neovim

### install

```
brew install neovim
```

### setting

```
~/.config/nvim/init.vim
```

ni

```
source ~/.vimrc
```

de

```
ln -s ~/wrk/cnf/vim/.vimrc ~/.vimrc
```

### syntax

```
ln -s ~/wrk/cnf/vim/cnf/syntax.mac syntax
```


### vim-plug

```
sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs \
       https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
```


### fzf-vim

vim de

```
:PlugInstall
```


## fish

### install

```
brew install fish
```

### setting

```
~/.config/fish/config.fish
```

ni

```
source ~/.config/fish/config_env.fish
```


## fd

```
brew install fd
```


## rg

```
brew install ripgrep
```


## zoxide

### install

```
brew install zoxide
```

### setting

```
zoxide init fish | source
```


## fzf

```
brew install fzf
```


## tmux

```
brew install tmux
```


## trans

```
brew install translate-shell
```


## node-js

```
wip:
```


