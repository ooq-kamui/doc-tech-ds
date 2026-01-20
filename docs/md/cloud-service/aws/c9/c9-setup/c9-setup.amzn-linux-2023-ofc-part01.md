
# c9 ( amazon linux 2023 ) setup part-01


amazon linux 2023

at bash


## brew

https://brew.sh/ja/

at 2024-05-26

事前に ec2-user の pw 設定をする

```
sudo passwd ec2-user
```

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

path setting

```
(echo; echo 'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"') >> /home/ec2-user/.bashrc
```

```
eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"
```


## fd

npm

```
npm install -g fd-find
```

or brew, next time


## rg ( ripgrep )

brew

```
brew install ripgrep
```


## fzf

```
git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf
```

```
~/.fzf/install
```


## vim-plug

vim

```
curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
```


## z

#### at bash

https://github.com/rupa/z

```
git clone https://github.com/rupa/z ~/wrk/app/z
```


### at fish

https://github.com/jethrokuan/z

```
fisher install jethrokuan/z
```

fish の install が先だった可能性あり, 記憶をなくした..


## fish

brew

```
brew install fish
```

```
(echo; echo 'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"') >> /home/ec2-user/.bashrc
```

```
eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"
```


## mmv

```
brew install itchyny/tap/mmv
```


## pwsh

```
curl https://packages.microsoft.com/config/rhel/9/prod.repo | sudo tee /etc/yum.repos.d/microsoft.repo
```

```
sudo yum install -y powershell
```

ref

https://www.genspark.ai/spark/how-to-install-powershell-on-amazon-linux-2023-a-comprehensive-guide/cb188f0a-883f-4f72-937e-5343ba9822c4


## neovim

```
brew install neovim
```

### vim-plug

```
sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs \
       https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
```


### syntax

```
cd ~/.config/nvim
```

```
ln -s ~/wrk/cnf/vim/cnf/syntax.c9 syntax
```


