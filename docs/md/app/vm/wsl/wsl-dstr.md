
# wsl distro


## install されている distro を表示

```
wsl --list --verbose
```

- state も確認できる

ex

```
_ wsl --list --verbose
  NAME                      STATE           VERSION
* AlmaLinux-10              Running         2
  Ubuntu                    Stopped         2
  podman-machine-default    Stopped         2
_ 
```


## install できる distro を表示

```
wsl --list --online
```


## distro を install

```
wsl --install -d <distro>
```


## distro を del

```
wsl --unregister <distro>
```


