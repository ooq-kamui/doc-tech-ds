
# pwsh  -  color


## 設定できる箇所, 現在の setting の確認

```
$PSStyle.FileInfo | Get-Member
```


## 設定できる color

```
$PSStyle.Foreground | Get-Member
```

```
$PSStyle.Background | Get-Member
```


## color set

文字色 を設定する

```
$PSStyle.FileInfo.Directory = $PSStyle.Foreground.Cyan
```

文字色 と 背景色 を設定する

```
$PSStyle.FileInfo.Directory = $PSStyle.Foreground.White + $PSStyle.Background.Blue
```


