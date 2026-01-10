
# wsl


## install されている distro の確認

```
wsl --list --verbose
```

or

```
wsl -l -v
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


## export

```
wsl --export <distro-name> <file-name>.tar
```

ex

```
wsl --export AlmaLinux-10 alm-10.tar
```


## import

- dir を用意しておく必要がある

```
wsl --import <distro-name> <dir-name> <file-name>
```

ex

```
mkdir alm-10
```

```
wsl --import alm-10 alm-10 alm-10.tar
```


## safe mode

`.wslconfig` に次を設定

```
[wsl2]
safeMode = true
```


