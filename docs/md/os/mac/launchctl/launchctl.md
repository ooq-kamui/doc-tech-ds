
# launchctl  -  plist


```
<label> : xxx.plist の xxx
```


### 確認

```
launchctl list <label>

launchctl list | grep xx
```

### 登録

```
launchctl load ~/Library/LaunchAgents/<label>.plist
```

### 削除

```
launchctl unload ~/Library/LaunchAgents/<label>.plist
```

### テスト実行

```
launchctl start <label>
```


## pc 起動時に自動登録

### dir

```
~/Library/LaunchAgents/<label>.plist
```

symbolic link でも 可

手動登録するなら, 上記 dir でなくともよい
が, 通常, 再起動時には再登録されて欲しいので
上記 dir に ln を作成しておくのが妥当


## key について

```
Label                 launchd のジョブの名前
                      ファイル名と同じ ( label.plist )
ProgramArguments      実行するプログラム, オプション, 引数
                        arrayノードで指定
RunAtLoad             起動 タイミング
                        true の場合 launchd に launchd.plist がロードされたとき
StandardOutPath       標準出力ファイル
                        省略時は /var/log/system.log
StandardErrorPath     標準エラーファイル

StartCalendarInterval 実行日時のカレンダー指定
  Weekday             0,7:sun, 1:mon, ...

StartInterval         実行日時のインターバル指定
```


## sample

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
  <dict>
    <key>Label</key>
    <string>kanonji.gnump3d</string>
    <key>ProgramArguments</key>
    <array>
      <string>/usr/bin/gnump3d</string>
      <string>--fast</string>
    </array>
    <key>StartCalendarInterval</key>
    <dict>
      <key>Weekday</key>
      <integer>3</integer>
      <key>Hour</key>
      <integer>0</integer>
      <key>Minute</key>
      <integer>0</integer>
    </dict>
    <key>StandardOutPath</key>
    <string>/Users/mofu/script/test2.out</string>
    <key>StandardErrorPath</key>
    <string>/Users/mofu/script/test2.err</string>

    <key>RunAtLoad</key>
    <false/>
    <key>KeepAlive</key>
    <false/>
  </dict>
</plist>
```



