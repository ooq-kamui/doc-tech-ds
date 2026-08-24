
# .bash_profile と .bashrc の違い


## launch mode

### login shell

- `.bash_profile` ( or `.profile` )
- case
  - SSH ログイン
  - mac, terminal 初回起動
  - `su -`
- 役割
  - ログイン時に 1 回だけ 実行される
  - 環境変数の設定
    - `export PATH=...`
    - `export EDITOR=...`
  - 子プロセスに引き継がれるべき設定を置く


### non-login interactive shell

- `.bashrc`
- case
  - 既にログイン済みの状態から新しい bash を開く
  - linux, terminal
- 役割
  - 対話的シェルが開くたびに 実行される
  - シェルセッション固有の設定を書く場所
    - エイリアス
    - プロンプト (`PS1`)
    - シェル関数
    - `shopt` オプション


## よくあるパターン

login shell は `.bashrc` を読まないので,
`.bash_profile` の中から明示的に `.bashrc` を読み込む書き方が定番

```
# ~/.bash_profile
if [ -f ~/.bashrc ]; then
    source ~/.bashrc
fi
```

こうすることで, login shell でも non-login shell でも
`.bashrc` の設定が常に有効になる


## mac と linux の違い

- mac: ターミナルを開くたびに login shell が起動する
  - `.bash_profile` が毎回読まれる
- linux ( GUI ): ターミナルエミュレータは通常 non-login shell
  - `.bashrc` が読まれる

この違いがあるため, 上記の `source ~/.bashrc` パターンを使っておけば,
どちらの OS でも設定が統一されて混乱しにくくなります


