
# redirect


## 基本

location で 設定する


## 設定箇所, 書式

`/etc/nginx/nginx.conf` に
default の `nginx.conf` に `location` の 記述があるので,
それを参考に記述

たいていは 443 に 記述すると思うので, そこに記述


## prefix

```
=     完全一致
^~    前方検索
~     正規表現
~*    正規表現
なし  前方検索
```

優先順位も上記の順



## ref

https://blog.grasys.io/post/tsunoda/nginx-rewrite/

https://heartbeats.jp/hbblog/2012/04/nginx05.html


