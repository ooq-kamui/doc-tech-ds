
# ar list


## def

```
$arlst = New-Object System.Collections.ArrayList
```

or

```
$ar = [System.Collections.ArrayList]::new()
```

or

```
[System.Collections.ArrayList] $ar = @( 0, 1, 2 )

# ^ confirm
```


## add

```
[void]$ar.Add('val')
```


## `??`

```
[void] $arlst.AddRange( ("bbb","ccc") )
```


## ref

https://learn.microsoft.com/ja-jp/powershell/scripting/learn/deep-dives/everything-about-arrays?view=powershell-7.4



