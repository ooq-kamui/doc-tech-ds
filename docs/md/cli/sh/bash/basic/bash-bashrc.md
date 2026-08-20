
# .bash_profile と .bashrc の違い

核心は **bash の起動モード** によって読み込まれるファイルが異なる, という点です.


## 起動モードの分類

| モード | 条件 | 読むファイル |
|--------|------|-------------|
| login shell | SSH ログイン, `su -`, ターミナルの初回起動 (macOS) など | `.bash_profile` (または `.profile`) |
| non-login interactive shell | 既にログイン済みの状態から新しい bash を開く (Linux のターミナルエミュレータなど) | `.bashrc` |


## それぞれの役割

### .bash_profile

- **ログイン時に 1 回だけ** 実行される
- 環境変数の設定 (`export PATH=...`, `export EDITOR=...` など) を書く場所
- 子プロセスに引き継がれるべき設定を置く

### .bashrc

- **対話的シェルが開くたびに** 実行される
- エイリアス, プロンプト (`PS1`), シェル関数, `shopt` オプションなど, シェルセッション固有の設定を書く場所


## よくあるパターン

login shell は `.bashrc` を読まないので, `.bash_profile` の中から明示的に `.bashrc` を読み込む書き方が定番です:

```bash
# ~/.bash_profile
if [ -f ~/.bashrc ]; then
    source ~/.bashrc
fi
```

こうすることで, login shell でも non-login shell でも `.bashrc` の設定が常に有効になります.


## macOS と Linux の違い

- **macOS**: ターミナルを開くたびに login shell が起動する -> `.bash_profile` が毎回読まれる
- **Linux (GUI)**: ターミナルエミュレータは通常 non-login shell -> `.bashrc` が読まれる

この違いがあるため, 上記の `source ~/.bashrc` パターンを使っておけば, どちらの OS でも設定が統一されて混乱しにくくなります.


