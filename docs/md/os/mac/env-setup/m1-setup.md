
# mac m1, setting init, install


## brew

https://zenn.dev/myb/articles/4b1dd3821703aa2ac95b


## fish

上記の brew を install してから

```
brew install fish
```


## tmux

https://zenn.dev/shuntaka/articles/6ff213d965afcb41ac4f

```
export PATH=/opt/local/bin:$PATH # MacPortsのPAHTを通す
```

```
sudo port install -f tmux
```


## vim

初めから入っている


## vim-plug

https://qiita.com/kouichi_c/items/e19ccf94b8e5ab6ed18e

```
curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
  https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
```


## fzf

https://zenn.dev/shuntaka/articles/6ff213d965afcb41ac4f

```
sudo port install -f fzf
```


## rg

https://zenn.dev/shuntaka/articles/6ff213d965afcb41ac4f

https://qiita.com/chikoski/items/f973e551a71ed0179116

```
arch --x86_64 sh <(curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs )
cargo -v  128  export PATH="$HOME/.cargo/bin:$PATH"
cargo install ripgrep
```

```
rustup self uninstall
```

```
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
cargo install ripgrep
cargo install fd-find
cargo install sd
cargo install bat
cargo install exa
```


## neovim

```
xcode-select --install
brew install --HEAD tree-sitter
brew install --HEAD luajit
brew install --HEAD neovim
```



