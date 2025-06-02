
# build


既存 image + Containerfile ( 命令 ) で image を作成する


## build

image を作成する

`Containerfile` のある dir で

```
podman image build -t <image-name> .
```

確認

```
podman image ls
```


## option

```
-t    作成する image name を指定
```






