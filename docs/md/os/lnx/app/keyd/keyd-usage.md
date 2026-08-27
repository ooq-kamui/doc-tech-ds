
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

- key を押すと, keyd が remap したあとの出力が表示される
- もとの入力 key を見たい場合は, keyd を止めてから 実行する
  ```
  sudo systemctl stop keyd
  ```


### log の確認

```
sudo journalctl -eu keyd
```

- 設定 file に err がある場合は log に出る


## 緊急時の復旧 ( 重要 )

設定を間違えてキーボードが使えなくなった場合,  
以下の特殊キーシーケンス で keyd を強制終了できます

```
backspace + escape + enter
# 3 キー同時押し
```

- keyd が終了し, もとの keymap に戻ります


## layer

- keychron launcher などにもある, layer の機能があります
- layer name には `-` は使わないのが無難


## ids

- id の調べかた
  - `sudo keyd monitor` で 表示される `xxx:xxx:xxxxxx` の形式の文字列 が id
    - ex
      ```
      keyd virtual keyboard   0fac:0ade:bea394c0      y up
      ```


## app ごとの remap

- これは 応用, 実験的機能 です
- kde wayland での動作は `dbus-python` に依存します  
  必要に応じて `sudo dnf install python3-dbus` を入れてください

kde wayland でアプリごとに異なるリマップをしたい場合

```
# keyd グループに自分を追加
sudo usermod -aG keyd $(whoami)

# ログアウト・ログインで反映


# 設定ファイルを作成
mkdir -p ~/.config/keyd
vim ~/.config/keyd/app.conf
```

```
# ~/.config/keyd/app.conf の例
[firefox]
alt.l = C-l
alt.t = C-t
alt.w = C-w
```


