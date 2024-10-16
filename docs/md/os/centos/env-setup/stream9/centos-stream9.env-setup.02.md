
# centos stream 9  -  env setup part 02  -  ( sakura vps )


## git

いったん, git clone cnf のみ

user settng しなくても, clone はできる


## bash

.bashrc

```
LD_LIBRARY_PATH=/usr/local/lib64
export LD_LIBRARY_PATH
```


## vim

.vimrc の確認

```
echo $VIM
```

err, echo すら使えない ??


```
sudo dnf -y install vim-enhanced
```

よく分からないが,
これで, `vi` も `vim` も使えるようになる

```
which vim
/usr/bin/vim
```

```
which vi 
alias vi='vi -p'
        /usr/bin/vi
```


よくみると , nvim も何かのタイミングで, brew で入っている

nvim を使うことにする

```
mkdir ~/.config/nvim
```

```
vi ~/.config/nvim/init.vim
```

```
source ~/.vimrc
```


## fish

```
cd ~/.config/fish
```

```
vi config.fish
```

```
ln -s ~/wrk/cnf/sh/fish/fnc functions
```

cre 

```
vi ~/wrk/cnf/sh/fish/cnf/config_centos_c9.fish
```

```
alias ll 

# etc ..
```


## z ( d )

```
brew install z
```

err

```
==> Installing gcc
Error: An exception occurred within a child process:
  RuntimeError: /home/linuxbrew/.linuxbrew/opt/flex not present or broken
Please reinstall flex. Sorry :(
```

```
brew install flex
```

```
brew reinstall z
```

入ったが, brew のは fish では動かないぽい..


fisher のを入れる

```
fisher install jethrokuan/z
```

cnf fish fnc の既存のを削除して, try re, で, success



## git

```
ln -s ~/wrk/cnf/git/.gitconfig ~/
```



## fd



## rg



## fzf




## fzf.vim




## nginx

ref :
https://kinsta.com/jp/knowledgebase/install-nginx/


```
sudo yum install epel-release
```

```
sudo yum install nginx
```

launch

```
sudo systemctl start nginx
```

boot 時に自動的に起動

```
sudo systemctl enable nginx
```







