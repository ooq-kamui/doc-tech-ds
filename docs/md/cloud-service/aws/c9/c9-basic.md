
# cloud9


## os

amazon linux = red hat


## disc size mod

確認

```
df -h              # ディスク 確認
```

```
lsblk              # ブロック 確認
```


## 拡張 ( old )

- 現在は console からやれば ok

```
sudo growpart /dev/xvda 1    # partition 拡張
```

```
sudo xfs_growfs -d /         # file system 拡張
```



