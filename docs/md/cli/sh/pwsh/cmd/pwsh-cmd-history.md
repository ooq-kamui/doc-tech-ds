
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

- 下記の file から 手動編集で 削除しても可


## history file

```
(Get-PSReadlineOption).HistorySavePath
```

ex

```
C:\Users\xxx\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt
```


