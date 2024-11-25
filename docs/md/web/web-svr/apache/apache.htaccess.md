
# htaccess


## rewrite

```
wip:
```


## redirect

```
Redirect permanent url_bfr url_aft
```

```
RedirectMatch permanent url_ptn_bfr url_ptn_aft
```


## tips

### enable confirm

`.htaccess` が効いているのかがよくわからないとき

`ErrorDocument` を 仮で 設定してみて,

```
ErrorDocument 404 https://google.com
```

存在しない page に access して, 上記の site に飛べば, 効いている,
と判断できます



