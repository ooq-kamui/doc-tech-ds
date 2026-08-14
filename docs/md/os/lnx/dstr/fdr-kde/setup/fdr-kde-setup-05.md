
## fcitx 5, mozc ( iem )


### 手順

- package install
  ```
  sudo dnf install fcitx5 fcitx5-mozc fcitx5-configtool fcitx5-qt fcitx5-gtk kcm-fcitx5 fcitx5-autostart
  ```
- fedora kde, restart
- virtual keyboard
  - system settings > keyboard > virtual keyboard
  - "Fcitx 5 Wayland Launcher" を 選択して, 設定
- input method
   - 1. システムトレイのキーボードアイコンを右クリック -> "設定 (Configure)" を選択
   - add input method
   - "Mozc" を 選択して設定


### desc

| パッケージ       | 役割                                                              |
|------------------|-------------------------------------------------------------------|
| fcitx5-mozc      | Fcitx 5 本体 + Mozc エンジン                                      |
| kcm-fcitx5       | KDE システム設定用の Fcitx 5 設定モジュール                       |
| fcitx5-autostart | 環境変数の設定 (`/etc/profile.d`) と XDG autostart ファイルを提供 |

> `fcitx5-autostart` が `XMODIFIERS`, `GTK_IM_MODULE`, `QT_IM_MODULE` を自動で設定してくれるため,
> 手動で環境変数を書く必要は基本的にない


