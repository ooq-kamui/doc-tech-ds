
# gitbash


## 初回起動

gitbash 本体を起動する( 初回は windows terminal から起動しない )

.bashrc などが適切に作成されないため


## 文字コード の設定

```
chcp.com 65001
```

gitbash の場合は `chcp` ではなく `chcp.com` なので注意


.bashrc などに 下記を追加

```
export LC_ALL=ja_JP.utf8
export LANG=ja_JP.utf8
export LANGUAGE=ja_JP.utf8
export LC_CTYPE="ja_JP.utf8"
export LC_NUMERIC="ja_JP.utf8"
export LC_TIME="ja_JP.utf8"
export LC_COLLATE="ja_JP.utf8"
export LC_MONETARY="ja_JP.utf8"
export LC_MESSAGES="ja_JP.utf8"
```


## cmdline での画面のちらつきを off にする

~/.inputrc

```
set bell-style none
```


## zoxide

pwsh から install する

.bashrc_gitbash などに下記を追加する

```
eval "$(zoxide init bash)"
```


## fzf

fzf を pwsh から install する

vim plugin を pwsh から install する

plug.vim を ~/.vim/autoload/plug.vim に設置する

gitbash の vim から plugin fzf.vim を install して `~/.vim/plugged/fzf/bin` を設置する

~/.fzf.bash を設置する

```
# Setup fzf
# ---------
if [[ ! "$PATH" == */c/Users/kamui/.vim/plugged/fzf/bin* ]]; then
  PATH="${PATH:+${PATH}:}/c/Users/kamui/.vim/plugged/fzf/bin"
fi

eval "$(fzf --bash)"
```



