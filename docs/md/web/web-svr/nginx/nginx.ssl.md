
# nginx  -  ssl


## 基本

一般的に site を ssl 化するときに必要なのは, 次の file

- key
- csr
- crt


作成方法は ssl の ページを参照



## nginx の設定

### main domain の場合

上記の file を所定の dir に置く

ここでは 下記の dir とする

```
/etc/nginx/ssl/
```

conf file

```
/etc/nginx/nginx.conf
```

内容を編集

```
server {
    listen 443 ssl;
    ssl_certificate     /etc/nginx/ssl/server.crt;
    ssl_certificate_key /etc/nginx/ssl/server.key;
}
```

nginx を再起動

```
sudo nginx -s reload
```

or

```
sudo systemctl restart nginx
```



## ref

https://cn.teldevice.co.jp/blog/p39750/

https://www.bestssl.net/faq/install-nginx/

https://qiita.com/clown0082/items/551d7c081ff6b41b1717



