
# obj

obj / dict / hash table

PSObject は別途記載


## ref

https://learn.microsoft.com/ja-jp/powershell/module/microsoft.powershell.core/about/about_hash_tables?view=powershell-7.4


## def

```
@{index=0; name="aiueo"; age=30}
```

改行ありの場合 `;` や `,` はいらない

```
$obj = @{
  index = 0
  name  = "aiueo"
  age   = 30
}
```

key に 日本語も ok

```
$obj = @{
  '日本語' = '日本語でok'
}
```


## get ( access )

```
$obj.key01
```

```
$obj['key01']
```


## add key val

```
$obj.Add('key02', $val)
```

下記でも ok

```
$obj.key03 = $val03
```


## set key val

```
$obj.key04 = $val04
```


## obj に 特定の key があるか

```
if ($obj.ContainsKey('key01')){
  echo "true"
}
```


