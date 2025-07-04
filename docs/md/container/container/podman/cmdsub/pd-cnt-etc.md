
# podman container


## container を stop する

```
podman stop <container-id>
```

### 直近に起動した container を stop する

```
podman stop -l
```


## container を削除

```
podman rm <container-id>
```

### すべての container を 削除

```
podman rm -a
```


## container 内 file cp

```
podman cp [op] container_name:file_path_01 container_name:file_path_02
```


