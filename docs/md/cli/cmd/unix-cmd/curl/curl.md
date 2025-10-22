
# curl


## file dl

```
curl -OL http://tomcat.apache.org/tomcat-8.5-doc/appdev/sample/sample.war
```

```
-O  dl file-name を指定
    指定がない場合は url の file-name のまま

-L  redirect 有効

```


## 疎通確認

```
curl -I ip_address:port_num
```

```
-I  : http レスポンスヘッダー を取得する
```



