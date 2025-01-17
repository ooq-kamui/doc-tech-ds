
# obj

obj / dict / hash table

PSObject は別途記載


## ref

https://learn.microsoft.com/ja-jp/powershell/module/microsoft.powershell.core/about/about_hash_tables?view=powershell-7.4


## def

```
@{index=0; name="aiueo"; age=30}
```

改行ありの場合 `;` はいらない

```
$obj = @{
  index = 0
  name  = "aiueo"
  age   = 30
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



