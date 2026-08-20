
# keyd  -  basic


## keyd とは

- keyd は linux の kernel レベル ( evdev ) で動く, key remap daemon
- x11 / wayland / tty を問わず, システム全体で動作する
- kde wayland でも使える
- https://github.com/rvaiya/keyd


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
- 元の入力 key を見たい場合は, keyd を止めてから 実行する
  ```
  sudo systemctl stop keyd
  ```


### ログの確認

```
sudo journalctl -eu keyd
```

- 設定ファイルにエラーがある場合はログに出る


## 緊急時の復旧 ( 重要 )

設定を間違えてキーボードが使えなくなった場合,
以下の特殊キーシーケンスで keyd を強制終了できます

```
backspace + escape + enter
# 3 キー同時押し
```

- keyd が終了し, 元のキーマップに戻ります


## layer

wip

- layer name には `-` は使わないのが無難


## ids

- id の調べかた
  - `sudo keyd monitor` で,
    1 col 目に 表示される `xxx:xxx` の形式の文字列が id




---

## アプリごとのリマップ ( 応用, 実験的機能 )

kde wayland でアプリごとに異なるリマップをしたい場合

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

ただしこの機能は実験的で, kde wayland での動作は `dbus-python` に依存します  
必要に応じて `sudo dnf install python3-dbus` を入れてください


