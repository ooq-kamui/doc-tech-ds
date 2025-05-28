
# build


既存 image + 命令 ( ContainerFile ) で image を作成する


## ContainerFile

ex

```
FROM docker.io/centos/httpd-24-centos7
```


## build

image を作成する

`ContainerFile` のある dir で

```
podman build -t <image-name> .
```

確認

```
podman images
```


## ContainerFile で使える 命令

```
wip:
```




