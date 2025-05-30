
# tutorial 02  -  podman


## ref

https://tech-lab.sios.jp/archives/27666


## step : container 起動

```
podman run -dt -p 8080:8443/tcp --name test-container-7 centos/httpd-24-centos7
```

これのやっていること

- `centos/httpd-24-centos7` を元に container を起動
- `--name test-container` : `test-container` という名前にする
- `-p 8080:8443/tcp` : 元pc の port 8080 を container 内の port 8443 に割り当てる

確認

```
podman ps
```


## step : container 内 に 入って file 操作

container 内 に bash で 入る

```
podman exec -it test-container-7 /bin/bash
```

container 内 で

```
cat /etc/httpd/conf/httpd.conf | grep DocumentRoot
```

```
echo -e "This is test content DESU.\n Made with bash in Container." > /opt/rh/httpd24/root/var/www/html/test_exec.html
```

container から抜ける

```
exit
```

元pc で

```
curl -k https://localhost:8080/test_exec.html
```

```
curl: (35) OpenSSL SSL_connect: SSL_ERROR_ZERO_RETURN in connection to localhost:8080
```

になる, いったん, 次へ進む



## step : cp

```
echo "aaa" > tmp.html
```

```
podman cp tmp.html test-container-7:/opt/rh/httpd24/root/var/www/html/
```


確認

```
podman exec -it test-container-7 /bin/bash
```

```
ls -la /opt/rh/httpd24/root/var/www/html/
```


## step : image の作成 ( build )

Containerfile

```
vi Containerfile
```

```
FROM docker.io/centos/httpd-24-centos7
RUN echo "new file with Containerfile" > /opt/rh/httpd24/root/var/www/html/test.html
COPY ./test_containerfile.html /opt/rh/httpd24/root/var/www/html/COPY.html
```

```
echo -e "podman build test file. \n copy from local file" > ./test_containerfile.html
```

```
podman build -t tst-build .
```

確認

```
podman images
```

```
podman exec -it tst-build /bin/bash
```

```
ls -la /opt/rh/httpd24/root/var/www/html/
```


