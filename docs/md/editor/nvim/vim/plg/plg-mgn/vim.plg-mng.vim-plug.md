
# vim-plug


## official site

https://github.com/junegunn/vim-plug


## vim-plg 自体の install

### vim

#### unix

```
curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
```

### nvim neovim

#### unix, linux

```
sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs \
       https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
```


## plugin の install

```
:PlugInstall
```

## plugin の del ( uninstall )

plugin の記述を削除 ( コメントアウト ) して

```
:PlugClean
```



