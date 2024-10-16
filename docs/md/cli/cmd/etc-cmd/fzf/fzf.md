
# fzf


## コマンドラインから

ファイル検索

```
ctl-t
```

コマンド履歴検索

```
ctl-r
```


preview window の customize

```
fzf --preview 'file {}' --preview-window down:1
```


## fzf.vim

```
let g:fzf_preview_window = ['up:40%:hidden', 'ctrl-/']
```


## rg

```
fzf#vim#grep(command, [has_column bool], [spec dict], [fullscreen bool])
```

```
command! -bang -nargs=* Rg
  \ call fzf#vim#grep(
  \   'rg --column --line-number --no-heading --color=always --smart-case -- '.shellescape(<q-args>),
  \   1,
  \   fzf#vim#with_preview(),
  \   <bang>0
  \ )
```


## pwsh で 日本語 path の文字化け

いまの設定を退避

```
$tmp=[System.Console]::OutputEncoding
```

設定を変更

```
[System.Console]::OutputEncoding=[System.Text.Encoding]::utf-8?
```

コマンド実行

戻す

```
[System.Console]::OutputEncoding=$tmp
```



