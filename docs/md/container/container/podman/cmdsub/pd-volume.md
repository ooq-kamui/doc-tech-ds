
# podman volume


## basic

host pc と container 内で volume ( dir / file ) を bind ( 同期 ) する


## volume list

```
podman volume ls
```


## 詳細 表示

```
podman volume inspect <vol-name>
```


## volume を作成する

```
podman volume create <vol-name>
```


## volume を削除する

```
podman volume rm <volume-name>
```


## volume を bind して container を起動

```
podman run -v <volume-name>:<container-dir>
```


## host-dir を bind して container を起動

```
podman run -v <host-dir>:<container-dir>
```



