
# alma linux 10 ( skr-vps )


## git

```
sudo dnf install git
```


## dotfiles

```
mkdir ~/wrk/prj-pri
cd    !$
```

```
git clone https://github.com/ooq-kamui/dotfiles
```


## bash

```
vim ~/.bashrc
```

```
test -f ~/wrk/prj-pri/dotfiles/sh/bash/bashrc/dflt/.bashrc && source ~/wrk/prj-pri/dotfiles/sh/bash/bashrc/dflt/.bashrc
test -f ~/wrk/prj-pri/dotfiles/sh/bash/bashrc/c9/.bashrc   && source ~/wrk/prj-pri/dotfiles/sh/bash/bashrc/c9/.bashrc
```

```
cp ~/wrk/prj-pri/dotfiles/sh/bash/bashrc/c9/.colorrc ~/
```


## brew

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

```
echo >> ~/.bashrc
```

```
echo 'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"' >> ~/.bashrc
```

```
eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"
```


## neovim ( nvim )

```
brew install neovim
```


## fd

```
brew install fd
```


## zoxide

```
brew install zoxide
```


## rg ( ripgrep )

```
brew install ripgrep
```


## fzf

```
brew install fzf
```


## fish

```
brew install fish
```

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


## neovim ( nvim )

```
mkdir ~/.config/nvim
```

```
ln -sin ~/wrk/prj-pri/dotfiles/nvim/scrpt/init.lua .
```

```
ln -sin ~/wrk/prj-pri/dotfiles/nvim/scrpt/lua .
```

```
ln -sin ~/wrk/prj-pri/dotfiles/nvim/syntax/c9 syntax
```

confirm

```
_ ll
total 0
lrwxrwxrwx 1 50 2025-06-20 09:21 init.lua -> /home/alm/wrk/prj-pri/dotfiles/nvim/scrpt/init.lua
lrwxrwxrwx 1 45 2025-06-20 09:22 lua -> /home/alm/wrk/prj-pri/dotfiles/nvim/scrpt/lua
lrwxrwxrwx 1 45 2025-06-20 09:23 syntax -> /home/alm/wrk/prj-pri/dotfiles/nvim/syntax/c9
```

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


## git

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
git remote set-url origin https://xxxxxxxxxxxxxxxx@github.com/ooq-kamui/xxx
```


## trns

```
brew install translate-shell
```


## node-js

```
brew install node
```


## lua

```
brew install lua
```


## podman

```
brew install podman
```


