
# strage size up


## aws console

instance stop

strage > volume の画面で size を入力, 反映

instance 再起動


confirm, c9 cmdline から

```
df -h
```

この時点で size が増えていれば, 下記はやらなくてもよい

すぐに反映されないときもあるが,
instance 再起動 を入念に行って, 確認し,
下記の cmdline からの手動変更はやらないほうが無難



## c9 cmdline

confirm

```
lsblk
```

confirm

```
df -h
```

partition expand

```
sudo growpart /dev/xvda 1
```

file system size up

```
sudo xfs_growfs /dev/xvda1
```

confirm

```
lsblk
```

confirm

```
df -h
```



