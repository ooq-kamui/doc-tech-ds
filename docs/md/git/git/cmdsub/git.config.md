
# git config


## config file path

```
local   repo/.git/config
global  ~/.gitconfig
system  /etc/gitconfig ( os によって dir は異なる )
```


## 基本

global の 確認, 設定

```
git config --global xxx xxx
```

local  の 確認, 設定

```
git config --local  xxx xxx
```

local の場合は 省略してもよい

```
git config xxx xxx
```



## 現在の設定を表示

```
git config --list
```


## user.name を設定する

```
git config user.name "ooq.kamui"
```

確認

```
git config user.name
```


## user.email を設定する

```
git config user.email "kamui@kamui.com"
```

確認

```
git config user.email
```


## default branch master > main

```
git config --global init.defaultBranch main
```


## 直接編集

comment

wip :

```
#?? comment
```



