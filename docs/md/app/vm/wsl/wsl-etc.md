
# wsl etc


## path に win ( /mnt/c/... ) の path を追加しない

`.wslconfig` に次を設定

```
[interop]
appendWindowsPath = false
```

確認 command

```fish
string match '*/mnt/*' $PATH
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


## safe mode

`.wslconfig` に次を設定

```
[wsl2]
safeMode = true
```


## wsl 上で, path を win の path に変換する

```
wsl.exe -w <path>
```


