
# ln -s

https://learn.microsoft.com/ja-jp/powershell/module/microsoft.powershell.management/new-item?view=powershell-7.4


## $target へのシンボリックリンクを $path として作る

管理者権限で login

```
New-Item -ItemType SymbolicLink -Path $path -Value $target
```


