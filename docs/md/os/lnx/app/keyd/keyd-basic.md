
# keyd  -  basic


## keyd とは

- keyd は linux の kernel レベル ( evdev ) で動くキーリマップデーモン
- x11 / wayland / tty を問わず, システム全体で動作する
- kde wayland でも使える

https://github.com/rvaiya/keyd


## config file

```
sudo vim /etc/keyd/default.conf
```


## 設定の反映

```
sudo keyd reload
```


## key name view

```
sudo keyd monitor
```

- キーを押すと, keyd がリマップした後の出力が表示される
- 元の入力イベントを見たい場合は, 先に `sudo systemctl stop keyd` してから実行


### ログの確認

```bash
sudo journalctl -eu keyd
```

- 設定ファイルにエラーがある場合はログに出る


## 緊急時の復旧 ( 重要 )

設定を間違えてキーボードが使えなくなった場合, 以下の特殊キーシーケンスで keyd を強制終了できます

```
Backspace + Escape + Enter ( 3 キー同時押し )
```

これで keyd が終了し, 元のキーマップに戻ります


## アプリごとのリマップ ( 応用, 実験的機能 )

KDE Wayland でアプリごとに異なるリマップをしたい場合

```bash
# keyd グループに自分を追加
sudo usermod -aG keyd $(whoami)

# ログアウト・ログインで反映


# 設定ファイルを作成
mkdir -p ~/.config/keyd
vim ~/.config/keyd/app.conf
```

```ini
# ~/.config/keyd/app.conf の例
[firefox]
alt.l = C-l
alt.t = C-t
alt.w = C-w
```

ただしこの機能は実験的で, KDE Wayland での動作は `dbus-python` に依存します  
必要に応じて `sudo dnf install python3-dbus` を入れてください


## まとめ

```bash
# 全体の流れ ( コピペ用 )
sudo dnf copr enable alternateved/keyd
sudo dnf install keyd
sudo systemctl enable --now keyd
sudo vim /etc/keyd/default.conf   # 設定を書く
sudo keyd reload                  # 反映
```



