
# git config


## config file path

```
local   repo/.git/config
global  ~/.gitconfig
system  /etc/gitconfig ( os によって dir は異なる )
```


## 基本

### global の 確認, 設定

```
git config --global xxx xxx
```

### local  の 確認, 設定

```
git config --local  xxx xxx
```

省略した場合は local の 確認, 設定

```
git config xxx xxx
```


## 現在の設定を 一覧 表示

```
git config --list
```


## user.name を設定する

```
git config user.name "ooq-tiki"
```

確認

```
git config user.name
```


## user.email を設定する

```
git config user.email "ooq.tiki@gmail.jp"
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



