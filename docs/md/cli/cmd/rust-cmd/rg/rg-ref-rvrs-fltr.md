
# filter 関連  -  逆引き


## file 拡張子 を指定

```
rg ptn -g "*.lua"
```

or

```
rg ptn --glob="*.lua"
```


## file, dir, 名, 拡張子 などで除外 ( filter )

```
rg ptn -g "!*.lua"
```

or

```
rg ptn --glob="!*.lua"
```

or

`.ignore` file に設定



## tips

default で 隠しファイル ( .xxx ) は search 対象外

よって, `.gitignore` の内容も 検索されない


