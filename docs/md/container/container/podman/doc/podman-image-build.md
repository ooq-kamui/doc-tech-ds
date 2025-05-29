
# build


既存 image + 命令 ( Containerfile ) で image を作成する


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



