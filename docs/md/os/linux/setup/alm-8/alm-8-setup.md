
# alma linux 8


## sudo

su になる

```
su
```

sudoers を編集

```
visudo
```

対象 user を root と同じ設定にする


## yum

```
sudo yum update
```


## git

```
sudo yum install git
```


## brew

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

```
echo >> /home/alm/.bashrc
```

```
echo 'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"' >> /home/alm/.bashrc
```

```
eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"
```


## fish

```
brew install fish
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

```
brew install zoxide
```


## fzf

```
brew install fzf
```


## nvim

```
brew install neovim
```


## dotfiles

```
git clone https://github.com/ooq-kamui/dotfiles
```


### fish

```
vi ~/.config/fish/config.fish
```

```
if status is-interactive
  source ~/wrk/prj-pri/dotfiles/sh/fish/cnf/dflt/config.fish
  source ~/wrk/prj-pri/dotfiles/sh/fish/cnf/c9/config.fish
  pwd
end
```

```
ln -sin ~/wrk/prj-pri/dotfiles/sh/fish/fnc ~/.config/fish/functions
```


### nvim

```
mkdir ~/.config/nvim
```

```
vi ~/.config/nvim/init.vim
```

```
source ~/wrk/prj-pri/dotfiles/nvim/scrpt/dflt/init.vim
```

```
ln -sin ~/wrk/prj-pri/dotfiles/nvim/scrpt/dflt/lua ~/.config/nvim/lua
```

```
ln -sin ~/wrk/prj-pri/dotfiles/nvim/syntax/c9 ~/.config/nvim/syntax
```

vim plug

```
sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs \
       https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
```

```
vi
```

```
:PlugInstall
```


### bash

```
# my add
test -f ~/wrk/prj-pri/dotfiles/sh/bash/bashrc/dflt/.bashrc && source ~/wrk/prj-pri/dotfiles/sh/bash/bashrc/dflt/.bashrc
test -f ~/wrk/prj-pri/dotfiles/sh/bash/bashrc/c9/.bashrc   && source ~/wrk/prj-pri/dotfiles/sh/bash/bashrc/c9/.bashrc
eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"
eval "$(zoxide init bash)"
```

colorrc

```
ln -sin ~/wrk/prj-pri/dotfiles/sh/bash/bashrc/c9/.colorrc ~/.colorrc
```


### git

```
cp ~/wrk/prj-pri/dotfiles/git/global/.gitconfig ~/.gitconfig
```

user, email は del

```
vi ~/.gitconfig
```

at repository

```
git config --local user.name ooq-tiki
```

```
git config --local user.email ooq.tiki@gmail.com
```

```
git remote set-url origin xxxxxxxx
```


