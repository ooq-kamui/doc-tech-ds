
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


## run psql ( postgres )

ref
- https://zenn.dev/acntechjp/articles/99c4f460a553bd

ex

```
podman run -dt \
  --name cnt-psql \
  -p 5432:5432 \
  -e POSTGRES_USER=psql \
  -e POSTGRES_PASSWORD=psql \
  -e POSTGRES_DB=tst \
  -v ./db/data:/var/lib/postgresql/data \
  -v ./db/init:/docker-entrypoint-initdb.d \
  postgres
```


## run tomcat

```
podman run -dt --name cnt-tomcat -p 8081:8080 tomcat
```

```
podman exec -it cnt-tomcat /bin/bash
```

```
cd webapps
```

```
wget http://tomcat.apache.org/tomcat-8.5-doc/appdev/sample/sample.war
# curl -OL http://tomcat.apache.org/tomcat-8.5-doc/appdev/sample/sample.war
```

確認

http://localhost:8081/sample/


### connect psql

```
apt update
```

```
apt install vim
```

```
vim /usr/local/tomcat/conf
```

```
wip
```







