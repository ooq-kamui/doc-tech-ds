
# ar-list


## def

```
$arlst = New-Object System.Collections.ArrayList
```

or

```
$arlst = [System.Collections.ArrayList]::new()
```

or

```
[System.Collections.ArrayList] $arlst = @( 0, 1, 2 )

# ^ confirm
```


## add

```
[void] $arlst.Add('val')
```


## `range`

```
[void] $arlst.AddRange( ("bbb","ccc") )
```


## len

```
$arlst.Count
```


## last element

```
$arlst[-1]
```


## ref

https://learn.microsoft.com/ja-jp/powershell/scripting/learn/deep-dives/everything-about-arrays?view=powershell-7.4


