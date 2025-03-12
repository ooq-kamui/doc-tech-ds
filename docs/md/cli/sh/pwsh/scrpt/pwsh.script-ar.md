
# ar


## ref

https://learn.microsoft.com/ja-jp/powershell/module/microsoft.powershell.core/about/about_arrays?view=powershell-7.4


## def

```
$ar = @()
```

```
$ar = @(1, 2, 3)
```

改行ありの場合は, カンマがいらない

```
$ar = @(
  1
  2
  3
)
```


## add

```
$ar = @(1)

$ar += 2
```

### 多次元配列の場合

ref
https://qiita.com/tfz/items/7edf4e6ad0682160b6dd

```
[array] $ar = @(
  @('aa1', 'aa2'),
  @('bb1', 'bb2'),
);

# @前 の , が肝
$ar += ,@('cc1', 'cc2');
```


## ある値の idx

```
$idx = [Array]::IndexOf($ar, $val)
```


## cnd

### 配列に特定の値があるか

```
if ($ar.Contains($val)){
  echo "true"
}
```


