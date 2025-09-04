
# etc


## cmdline 入力候補 の設定

```
Set-PSReadLineOption -Colors @{ InlinePrediction = $PSStyle.Foreground.BrightCyan }
```

複数行で候補を表示する

https://zenn.dev/atsushifx/articles/pwsh-console-intelisense

```
Set-PSReadLineOption -PredictionSource HistoryAndPlugin
Set-PSReadLineOption -PredictionViewStyle ListView
Set-PSReadLineOption -Colors @{ InLinePrediction = [ConsoleColor]::Cyan }
```


## say

```
( New-Object -ComObject SAPI.SpVoice ).Speak("arigatou")
```


