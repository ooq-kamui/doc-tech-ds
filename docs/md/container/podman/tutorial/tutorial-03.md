
# tutorial 03  -  podman


## ref

https://tech-lab.sios.jp/archives/27953


## step : container から image を作成

```
podman run -dt -p 8080:8443/tcp --name tst-commit-container-01 docker.io/centos/httpd-24-centos7
```

```
podman exec -it tst-commit-container-01 /bin/bash
```

container 内 になんらかの確認のための変更を残す

```
exit
```

```
podman commit tst-commit-container-01 tst-commit-image-01
```

確認

作成した image から container を起動

```
podman run -dt -p 8081:8443/tcp --name tst-commit-container-02 localhost/tst-commit-image-01:latest
```

```
podman exec -it tst-commit-container-02 /bin/bash
```

container 内 の変更を確認する

```
exit
```


## step : image を file に書き出す


```
podman save -o tst-commit-image-01.tar localhost/tst-commit-image-01:latest
```


## step : image file から image を読み込む


```
podman load 
```










