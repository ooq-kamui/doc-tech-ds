
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


## len

```
$arlst.Count
```


## add

```
[void] $arlst.Add('val')
```


## concat ( 配列 連結 )

```
$lst01.AddRange($lst02)
```


## last element

```
$arlst[-1]
```


## ref

https://learn.microsoft.com/ja-jp/powershell/scripting/learn/deep-dives/everything-about-arrays?view=powershell-7.4


