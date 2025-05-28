
# tutorial 01  -  podman


## ref

https://tech-lab.sios.jp/archives/27478


## step

```
podman run -dt -p 8080:80/tcp docker.io/library/httpd
```

これがやっていること

- `docker.io/library/httpd` の docker image から container を 起動
- `-dt` : ??
- `-p 8080:80/tcp` : 元pc の port 8080 を container 内の port 80 に割り当てる


確認

```
curl http://localhost:8080
```


## step

```
podman run -dt -p 8081:80/tcp docker.io/library/httpd
```

これがやっていること

- `-p 8081:80/tcp` : 元pc の port 8081 を container 内の port 80 に割り当てる
- 他は 上と同じ

確認

```
curl http://localhost:8081
```


