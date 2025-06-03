
# Containerfile


## basic

`Containerfile` は build で使用する file

docker の場合は `Dockerfile`


ex

```
FROM docker.io/centos/httpd-24-centos7
```


## Containerfile で使える 命令

```
FROM    元の image を指定


USER    user を指定


RUN     command を実行


ENV     環境変数を設定


```


