
# fnc

## def

```
function fnc01 {
  param( $subcmd, $opt, $prm01 )

}
```


## return

```
function fnc01 {
  param( $subcmd, $opt, $prm01 )

  $ret = 1

  return $ret
}
```


## call

```
$result = fnc01 $arg01 $arg02
```

or

```
$result = ( fnc01 $arg01 $arg02 )
```


## args

### 基本

```
function fnc02(){

  param($prm01, $prm02)

  echo $prm01
}
```



### 可変長引数

可変長引数 は `param()` を使わないで, `$args` を使う

```
function fnc02(){

  # param($prm01, $prm02)

  echo $prm01
}
```



