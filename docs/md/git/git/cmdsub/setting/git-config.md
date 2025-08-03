
# git config


## config file path

```
local   repo/.git/config
global  ~/.gitconfig
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
git config user.email "ooq.tiki@gmail.com"
```

確認

```
git config user.email
```


## default branch master > main

```
git config --global init.defaultBranch main
```


## editor

### vim

```
git config --global core.editor vim
```

### nvim

```
git config --global core.editor "nvim -f"
```


## upstream branch

ex

main branch の場合

```
git config branch.main.remote origin
```

```
git config branch.main.merge refs/heads/main
```


## 直接編集

### file

```
~/.gitconfig
```

### comment

```
# comment
```


