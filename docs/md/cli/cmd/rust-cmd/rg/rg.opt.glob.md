
# glob  -  opt  -  rg


## glob filter 基本

### 対象とする の場合

```
rg ptn -g glob_ptn
```

or

```
rg ptn --glob=glob_ptn
```

以下からは, 省略しない形式で記載

ここで便宜的に, こちらを accept と呼ぶことにする ( ignore でないほうとして )
( 英語として適切かは不明 )



### ignore ( 無視 ) の場合

```
rg ptn --glob=!glob_ptn
```



## そもそも glob とは ?

unix shell の wild card のこと



## rg glob match について

- 指定した glob_ptn は file name or dir name に適用される
  - path に適用されるわけではない
- accept の場合, dir name には match しない
  - そもそも rg は file を処理対象とするものなので,  
    dir に match する という考えかたが ない と思われる
  - つまり, dir に match するのは, ignore の場合のみ
- dir に match させる場合, 末尾に `/` を付ける
  - windows の場合も `/` でよさそう
    - ( `\` でなくてよい の意味 )
- 部分文字列として match させたい場合は  
  `rg ptn --glob=*substr*`  
  とする



## use case

### filter by file ext

```
rg ptn --glob="*.lua"
```



