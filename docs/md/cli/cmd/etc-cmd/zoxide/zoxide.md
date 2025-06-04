
# zoxide


## ref

https://formulae.brew.sh/formula/zoxide



## install

### mac / linux

```
brew install zoxide
```

#### fish

config.fish

```
zoxide init fish | source
```


### win

winget

or

scoop


#### pwsh

```
wip:
```


## faq

### err case

#### `zoxide: unsupported version (got 0, supports 3)`

- ディスクの容量不足 とのこと
  - なのだが, そんなことはないのに出ていた ( 自分は )
- `.local/share/zoxide/db.zo` を削除すると とりあえず直る


