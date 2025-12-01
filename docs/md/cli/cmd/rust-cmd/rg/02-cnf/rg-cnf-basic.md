
# config file  -  rg

設定ファイル の 基本


## cnf file でできること

default の option を 記述しておける


## cnf file name

`.ripgreprc`



## cnf file path setting

上記の cnf file が具体的にどの file かを
環境変数に指定できる


### fish

```
set RIPGREP_CONFIG_PATH "$HOME/.ripgreprc"
```

confirm

```
echo $RIPGREP_CONFIG_PATH
```


### bash

```
export RIPGREP_CONFIG_PATH="$HOME/.ripgreprc"
```

confirm

```
echo $RIPGREP_CONFIG_PATH
```


