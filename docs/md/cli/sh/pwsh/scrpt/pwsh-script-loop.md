
# loop


## foreach

### list

```
foreach ($item in $list){

  $item
}
```


### obj

```
foreach($key in $ageList.keys){
  $message = '{0} is {1} years old' -f $key, $ageList[$key]
  Write-Output $message
}
```

ref
https://learn.microsoft.com/ja-jp/powershell/scripting/learn/deep-dives/everything-about-hashtable?view=powershell-7.5#iterating-hashtables


## for

```
for ($idx = 0; $idx -lt 10; $idx++){
  echo "$idx"
}
```


## continue

pwsh に continue はあります

```
foreach ($item in $list){
  if ($true){
    continue
  }
}
```


