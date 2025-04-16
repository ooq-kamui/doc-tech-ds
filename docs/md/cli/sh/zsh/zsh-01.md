
# zsh


## install

```
brew install zsh
```


## `.zshrc`

```
~/.zshrc
```


## prompt

```
export PS1="_ "
```

bash と同


## key-bind

```
function my_fnc() {

  # write logic
  # :
  # prmpt str : $BUFFER

  zle reset-prompt  # prmpt draw re
}

zle -N my_fnc       # fnc   : widget reg

bindkey '^A' my_fnc # <c-a> : call my_fnc
```


## alias

```
alias c='clear'
```


## fnc

```
function fnc01(){

  echo 'my fnc'
}
```

bash と同


## ref

https://qiita.com/ryuichi1208/items/2eef96debebb15f5b402

https://usagidoki.com/mac-zshrc-base/

https://qiita.com/ishidao/items/769b2e9acfc2ce4542b6

https://zenn.dev/sprout2000/articles/bd1fac2f3f83bc


