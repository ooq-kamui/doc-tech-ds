
# glob  -  opt  -  rg


## glob filter 基本

### 対象 ( accept ) とする の場合

```
rg ptn -g glob_ptn
```

or

```
rg ptn --glob=glob_ptn
```

以下からは, `--glob=glob_ptn` の形式で記載


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
  - windows の場合も `/` でよい
    - ( `\` でなくてよい の意味 )
- 部分文字列として match させたい場合は  
  `rg ptn --glob=*substr*`  
  とする



## use case

### filter by file ext

```
rg ptn --glob="*.lua"
```



## accept, ignore の指定が同時にある場合

wip:



## pwsh の場合 の注意

pwsh ( win ) で実行したとき, 疑問のあったことを記載

### `--glob="!dir\"` の escape について

- `--glob="!dir\"` の指定をするとき  
  `--glob="\!dir/"` のように,  
  `!` を escape しなければ err になるときがある気がしている
- espace していなくても, 大丈夫なときも ある気がしている

### vim cmdline から実行 の場合

wip:


### fzf.vim から実行 ( call fzf#vim#grep() ) の場合

wip:



