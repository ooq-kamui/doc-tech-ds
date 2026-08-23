
## call fish fnc from bash


## method

**結論:** fish の autoload 機構(`~/.config/fish/functions/*.fish` に1関数1ファイル)を利用し、`fish -c "関数名 $argv"` を呼ぶ薄いラッパーを bash/zsh の PATH 上に置けば、相互依存も含めて自然に動きます

## 前提: 関数を autoload 化する

すでに `~/.config/fish/functions/` に1ファイル1関数で保存されているなら不要ですが、`config.fish` 内にベタ書きしている関数があれば先に保存します。

```fish
funcsave myfunc1
funcsave myfunc2
```

これが重要な理由: fish は関数呼び出し時に未定義の関数名をこのディレクトリから自動ロードします。なので `myfunc1` が内部で `myfunc2` を呼んでいても、`myfunc2.fish` が同じディレクトリにあれば **自分で明示的に source しなくても** 自動的に読み込まれます。相互依存の管理を自分でやる必要がありません。

## 汎用ディスパッチャを1つ作る

```bash
mkdir -p ~/bin
cat > ~/bin/fish-dispatch << 'EOF'
#!/usr/bin/env bash
exec fish -c "$(basename "$0") \$argv" "$@"
EOF
chmod +x ~/bin/fish-dispatch
```

ポイント:
- `basename "$0")` で「どの名前で呼ばれたか」を取得し、そのままfish関数名として使う
- `\$argv` は fish 側の変数展開として渡し、`"$@"` は bash 側からの実引数をそのまま fish に operands として渡す形。fish は `-c COMMAND` の後ろに続く追加の引数を `$argv` として使えるので、スペースや特殊文字を含む引数もクォート崩れなく渡せます
- `exec` で余計なプロセスを残さない

## 各関数名へのシンボリックリンクを一括生成

```bash
for f in ~/.config/fish/functions/*.fish; do
  name=$(basename "$f" .fish)
  ln -sf ~/bin/fish-dispatch ~/bin/"$name"
done
```

これで `~/.config/fish/functions/` 配下にある全関数が `~/bin/関数名` というコマンドとして生えます。`~/bin` が bash/zsh の `PATH` に入っていれば、

```bash
myfunc1 --foo bar
```

のように普通のコマンドとして呼べます。新しい関数を追加したら、上のループをもう一度回すだけで反映できます(`~/.zshrc` / `~/.bashrc` に関数追加スクリプトとして仕込んでおくと楽です)。

## 注意点

- **終了ステータス**: `fish -c` の exit code はそのまま親プロセスに伝播するので `$?` は問題なく使えます
- **対話的な機能**: `read` や補完など fish 依存の対話処理を使っている関数は、非対話 `-c` 実行だとうまく動かないことがあります(通常のコマンドライン処理なら問題なし)
- **環境変数**: fish と bash/zsh で `PATH` や環境変数の設定方法が違う場合、fish 側の `config.fish` が読み込まれた状態で実行されるので、bash 側の環境と差異が出ることがあります
- **起動コスト**: 呼び出しごとに fish プロセスを起動するので、ループの中で大量に呼ぶような用途には向きません(頻繁に使うなら都度 fish のログイン負荷を軽くしておくと良いです)

もし関数の数が少ない(数個程度)なら、シンボリックリンクを使わず bash/zsh 側に直接ラッパー関数を書く方法でも十分です:

```bash
# ~/.zshrc など
myfunc1() { fish -c "myfunc1 \$argv" "$@"; }
myfunc2() { fish -c "myfunc2 \$argv" "$@"; }
```

数が多い・今後も増える前提なら上のディスパッチャ方式が管理が楽です。


