
## call fish fnc, like bash cmd


## method

### bash の dispatch を 作る

```
~/bin/fish-dispatch
```

```
#!/usr/bin/env bash
exec fish -c "$(basename "$0") \$argv" "$@"
```

```
chmod +x ~/bin/fish-dispatch
```

- `basename "$0")` で「どの名前で呼ばれたか」を取得し、そのままfish関数名として使う
- `\$argv` は fish 側の変数展開として渡し,  
  `"$@"` は bash 側からの実引数をそのまま fish に operands として渡す
- fish は `-c COMMAND` の後ろに続く追加の引数を `$argv` として使えるので, 
  スペースや特殊文字を含む引数もクォート崩れなく渡せる
- `exec` で余計なプロセスを残さない


## dispatch への symbolic link を 作る

```
set fnc_name_lst ( ls ~/fish-fnc/*.fish )

for fnc_name in $fnc_name_lst

  ln -sin fish-dispatch ( basename $fnc_name .fish )
end
```


## notice

- 終了ステータス: `fish -c` の exit code はそのまま親プロセスに伝播するので `$?` は問題なく使えます
- 対話的な機能: `read` や補完など fish 依存の対話処理を使っている関数は,  
  非対話 `-c` 実行だとうまく動かないことがあります  
  ( 通常のコマンドライン処理なら問題なし )
- 環境変数: fish と bash で `PATH` や環境変数の設定方法が違う場合,  
  fish 側の `config.fish` が読み込まれた状態で実行されるので,  
  bash 側の環境と差異が出ることがあります
- 起動コスト: 呼び出しごとに fish プロセスを起動するので,  
  ループの中で大量に呼ぶような用途には向きません  
  (頻繁に使うなら都度 fish のログイン負荷を軽くしておくと良いです)


