
# nginx  -  sub domain


## sub domain の設定

conf file

```
/etc/nginx/conf.d/virtualhost.conf
```

ex

```
/etc/nginx/conf.d/tiki.ooq.jp.conf
```


設定内容

ex

```
server {
    listen 80;
    server_name tiki.ooq.jp;
    root /usr/share/nginx/html/sub;

    location / {
        index index.html;
    }
}
```


