
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


### array, array-list の return

要素数 1 の array, array-list を return すると,
勝手に 配列でなくなる

これの回避

`,` を return につける

```
function fnc01 {
  param()

  $arlst = @( 1 )

  return ,$arlst
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

  echo $args
}
```


### wildcard

```
function fnc03(){

  nvim -p ( Get-ChildItem $args )
}
```

`Get-ChildItem -Nmae` としなくてよい,
すると逆に err


