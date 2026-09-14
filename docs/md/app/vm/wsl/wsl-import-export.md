
# wsl import / export


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


### wsl に login したとき, su になってしまう

- これを回避する方法
- この現象は import した distro で起きる
- distro 環境の中の 下記の file を編集
- wsl 再起動

```conf title='/etc/wsl.conf'
[user]
default=<user-name>
```


## export

```
wsl --export <distro-name> <file-name>.tar
```

ex

```
wsl --export AlmaLinux-10 alm-10.tar
```


