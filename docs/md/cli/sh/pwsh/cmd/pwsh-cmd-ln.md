
# ln -s


## ref

https://learn.microsoft.com/ja-jp/powershell/module/microsoft.powershell.management/new-item?view=powershell-7.4


## `$target` へのシンボリックリンクを `$path` として作る

login as admin

```
New-Item -ItemType SymbolicLink -Path $path -Value $target
```

ex

```
New-Item -ItemType SymbolicLink -Path lua -Value C:\Users\xxx\wrk\prj-pri\dotfiles\nvim\scrpt\lua
```

```
New-Item -ItemType SymbolicLink -Path syntax -Value C:\Users\xxx\wrk\prj-pri\dotfiles\nvim\syntax\pwsh
```


