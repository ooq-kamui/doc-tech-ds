
# podman run


## container を 起動する, image から

```
podman run <image-name>
```


## option

```
-d          detached mode

-i          ???

-t  --tty   tty 端末 を用意する

    --name  container-name を付ける

    --rm    使い捨ての container を作成

-p          port の設定をする
            <host-port>:<cntinr-port>
            ex
            8080:80

-v          volume の設定をする

            <volume-name>:<cntinr-dir>
            ex
            pod-vol-01:/vol-01

            <host-dir>:<dir>
            ex
            ./pod-vol-02:/vol-02

-e          環境変数 の 設定


```

ex

```
podman run -dt --name container_001 img_001
```





