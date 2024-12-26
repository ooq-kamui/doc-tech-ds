
# history  -  pwsh


https://learn.microsoft.com/ja-jp/powershell/module/microsoft.powershell.core/clear-history?view=powershell-7.4


## history list

```
Get-History
```


## history delete

id で delete

```
Clear-History -Id 3, 5
```



## history file

```
(Get-PSReadlineOption).HistorySavePath
C:\Users\mura\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt
```



