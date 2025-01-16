
# fnc

## def

```
function fnc01 {
  param( $subcmd, $opt, $prm01 )

}
```


## args

可変長引数は `param()` を使わないで, `$args` を使う

```
function fnc02(){

  # param($prm01, $prm02)

  echo $args
}
```


