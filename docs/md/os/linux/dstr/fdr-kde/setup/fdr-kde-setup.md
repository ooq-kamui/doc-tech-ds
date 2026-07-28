
# fedofa kde plasma


## ssh

- ssh 接続を受け付けるようにする

```
wip
```


## zscaler

- office 環境 の hyper-v への install などで, 本体 pc に zscaler の chk が入っている場合,  
  本体の fedora install, 初回 launch 後,  
  できるだけ早い段階で zscaler の crt を 設定する必要があります
- ssh 接続を受け付けるようにする ( 上記 )


wip


## etc tool install

- 下記のあたりを dnf で install

```
sudo dnf install git      # installed ??

sudo dnf install fish

sudo dnf install fd-find
sudo dnf install ripgrep
sudo dnf install zoxide

sudo dnf install fzf

sudo dnf install neovim
```


## fcitx 5, mozc ( iem )


```
sudo dnf install fcitx5 fcitx5-mozc fcitx5-configtool fcitx5-qt fcitx5-gtk kcm-fcitx5 fcitx5-autostart
```


---

以下, Fedora KDE (Wayland) をインストールした直後の状態から, Fcitx 5 + Mozc で日本語入力を有効にするまでの手順です.

---

### 1. パッケージのインストール

```bash
sudo dnf install fcitx5-mozc kcm-fcitx5 fcitx5-autostart
```

| パッケージ       | 役割                                                              |
|------------------|-------------------------------------------------------------------|
| fcitx5-mozc      | Fcitx 5 本体 + Mozc エンジン                                      |
| kcm-fcitx5       | KDE システム設定用の Fcitx 5 設定モジュール                       |
| fcitx5-autostart | 環境変数の設定 (`/etc/profile.d`) と XDG autostart ファイルを提供 |

> `fcitx5-autostart` が `XMODIFIERS`, `GTK_IM_MODULE`, `QT_IM_MODULE` を自動で設定してくれるため,
> 手動で環境変数を書く必要は基本的にない

---

### 2. ログアウト -> 再ログイン

インストール後, 一度ログアウトして再ログインする.
これにより `fcitx5-autostart` が提供する環境変数とオートスタートが有効になる.

---

### 3. KDE で仮想キーボードとして Fcitx 5 を選択

1. システム設定 (System Settings) を開く
2. キーボード (Keyboard) -> 仮想キーボード (Virtual Keyboard) に移動
3. "Fcitx 5" または "Fcitx 5 Wayland Launcher" を選択し, "適用 (Apply)" をクリック

> Wayland ネイティブアプリで日本語入力を使うにはこの設定が必須

---

### 4. Mozc を入力メソッドとして追加

1. システムトレイのキーボードアイコンを右クリック -> "設定 (Configure)" を選択
2. "入力メソッドを追加 (Add Input Method)" をクリック
3. 検索欄に "mozc" と入力
4. "Mozc" (Japanese カテゴリ) を選択して追加
5. "適用 (Apply)" をクリック

> "Keyboard - English (US)" はそのまま残しておくこと. これが英語直接入力として切り替え先になる

---

### 5. 動作確認

任意のアプリケーションで `Ctrl+Space` を押すと, 英語入力と Mozc (日本語入力) が切り替わる.
ローマ字を入力するとひらがな・漢字の変換候補が表示される.

---

### 補足: 切り替えキーの変更

デフォルトの `Ctrl+Space` 以外のキー (例: 半角/全角キー) を使いたい場合は,
Fcitx 5 の設定画面 -> "全体の設定 (Global Options)" -> "入力メソッドの切り替え (Trigger Input Method)" から変更できる.

---



