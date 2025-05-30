
# build


既存 image + Containerfile ( 命令 ) で image を作成する


## build

image を作成する

`Containerfile` のある dir で

```
podman build -t <image-name> .
```

確認

```
podman images
```



