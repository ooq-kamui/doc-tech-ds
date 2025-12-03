
# wsl confirm


## install されている distro の確認

```
wsl --list --verbose
```


## wsl が使用している disc size

```
wsl df -h /
```

or

```
wsl --system -d <distro-name> df -h /mnt/wslg/distro
```

ex

```
_ wsl --system -d AlmaLinux-10 df -h /mnt/wslg/distro
```

