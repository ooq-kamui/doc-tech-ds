
# pwsh


## profile

### path

normal

```
$home\Documents\PowerShell
```

one drive

```
$home\OneDrive\Documents\PowerShell
```


## env:path

add

ex

```
$ENV:Path += ";$home\wrk\app\gcal\bin"
```


## 既存の cmd を overwrite する

dmy の function 名 を作り, alias `-Option AllScope` で上書きする

```
function dir_dmy {
  param( $path )

  z $path
}
Set-Alias dir "dir_dmy" -Option AllScope # cannot be removed
```


## bell sound off

```
Set-PSReadlineOption -BellStyle None
```


