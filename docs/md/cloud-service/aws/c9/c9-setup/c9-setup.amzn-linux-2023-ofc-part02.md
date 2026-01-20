
# c9 ( amazon linux 2023 ) setup part-02


## ec2-user の pw

```
sudo passwd ec2-user
```


## git

- git は 初期状態から 入っている


## dotfiles

```
mkdir -p ~/wrk/prj-pri
```

```
cd ~/wrk/prj-pri
```

```
git clone https://github.com/ooq-kamui/dotfiles
```

### bash

```
vim ~/.bashrc
```

```
# my add
test -f ~/wrk/prj-pri/dotfiles/sh/bash/bashrc/.bashrc       && source ~/wrk/prj-pri/dotfiles/sh/bash/bashrc/.bashrc
test -f ~/wrk/prj-pri/dotfiles/sh/bash/bashrc/.bashrc-linux && source ~/wrk/prj-pri/dotfiles/sh/bash/bashrc/.bashrc-linux
```

bash launch re


### colorrc

- wezterm の color-scheme にまかせる ので,  
  設定しない


## brew

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

```
echo 'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"' >> ~/.bashrc
```

bash launch re


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
fish
```

```
vi ~/.config/fish/config.fish
```

```
if status is-interactive
  source ~/wrk/prj-pri/dotfiles/sh/fish/cnf/config.fish
  source ~/wrk/prj-pri/dotfiles/sh/fish/cnf/config-linux-wsl.fish
  source ~/wrk/prj-pri/dotfiles/sh/fish/cnf/config-linux-alm.fish

  pwd
end
```


```
cd ~/.config/fish/
```

```
rm -rf functions
```

```
ln -sin ~/wrk/prj-pri/dotfiles/sh/fish/fnc functions
```

fish launch


## neovim ( nvim )

```
brew install neovim
```

```
mkdir ~/.config/nvim
```

```
cd ~/.config/nvim

```

```
ln -sin ~/wrk/prj-pri/dotfiles/nvim/scrpt/init.lua .
```

```
ln -sin ~/wrk/prj-pri/dotfiles/nvim/scrpt/lua .
```

confirm

```
_ ll
total 0
lrwxrwxrwx 1 50 2026-01-09 11:15 init.lua -> /home/alm/wrk/prj-pri/dotfiles/nvim/scrpt/init.lua
lrwxrwxrwx 1 45 2026-01-09 11:16 lua -> /home/alm/wrk/prj-pri/dotfiles/nvim/scrpt/lua/
```

```
sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs \
       https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
```


```
vi
```

plugin err 出るが とりあえず 無視

```
:PlugInstall
```

vim launch re


## git

### `~/.gitconfig` の編集

```
vi ~/wrk/prj-pri/dotfiles/git/global/.gitconfig ~/.gitconfig
```

- dotfiles の `.gitconfig` の内容 を 既存の `~/.gitconfig` へ手動でコピー編集
  - 既存の `~/.gitconfig` の
    - [credential] をつぶさない
    - [core] は上書き
  - user, email は コピーしない
  - その他は コピー


### at repository ( pri )

```
git config --local user.name ooq-tiki
```

```
git config --local user.email ooq.tiki@gmail.com
```

```
git remote set-url origin https://xxxxxxxxxxxxxxxx@github.com/ooq-kamui/xxx
```


## trans ( translate-shell )

```
brew install translate-shell
```


## node-js

- node は 初期状態から 入っている


## lua

```
brew install lua
```


## pwgen

```
brew install pwgen
```


## difft

```
brew install difftastic
```






