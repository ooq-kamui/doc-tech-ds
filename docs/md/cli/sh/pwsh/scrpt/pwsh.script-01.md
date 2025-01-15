
# pwsh script


## fnc

```
```


## fnc args

可変長引数は `param()` を使わないで, `$args` を使う

```
function fnc(){

  # param($p1, $p2)

  echo $args
}
```


## scope

### local var

```
$local:val = 1
```

### global var

```
$global:val = 1
```

### env var

```
$env:val = 1
```


## 改行を無視

バックゥォート を 行末に書く

ex

```
echo "aa   `
bb   "
```



