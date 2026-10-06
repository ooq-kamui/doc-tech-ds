
# zsh key-bind


- zsh では, key-bind に割り当てる関数を ZLE widget と呼びます  
- 手元の zsh で zle -la を実行し, cursor 移動に使う widget を抜き出しました
- 既定の key は emacs mode (bindkey -e) のものです


## 文字単位

```
^F, →    forward-char                        1 文字右へ
^B, ←    backward-char                       1 文字左へ
         vi-forward-char / vi-backward-char  vi 流の左右移動 (行端で止まる)
```


## 単語単位

```
M-f   forward-word                                            次の単語へ
M-b   backward-word                                           前の単語へ
      emacs-forward-word / emacs-backward-word                emacs 流の単語移動 (単語の末尾で止まる)
      vi-forward-word / vi-backward-word                      vi の w / b
      vi-forward-word-end / vi-backward-word-end              vi の e / ge
      vi-forward-blank-word / vi-backward-blank-word          vi の W / B (空白区切り)
      vi-forward-blank-word-end / vi-backward-blank-word-end  vi の E / gE
```


## 行内

```
^A   beginning-of-line                                行頭へ
^E   end-of-line                                      行末へ
     beginning-of-line-hist / end-of-line-hist        行頭・行末にいるときは、さらに前後の履歴へ移る
     vi-beginning-of-line / vi-end-of-line            vi の 0 / $
     vi-first-non-blank                               最初の非空白文字へ (vi の ^)
     vi-goto-column                                   指定した桁へ (vi の |)
     vi-find-next-char / vi-find-prev-char            vi の f / F
     vi-find-next-char-skip / vi-find-prev-char-skip  vi の t / T
     vi-repeat-find / vi-rev-repeat-find              vi の ; / ,
     vi-goto-mark / vi-goto-mark-line                 mark へ移動 (vi の ` / ')
```


## 複数行 buffer, 履歴 上下移動

```
            up-line                          buffer 内で 1 行上へ
            down-line                        buffer 内で 1 行下へ
^P/^N, ↑/↓  up-line-or-history               1 行上へ, 先頭行/最終行 にいるときは履歴を移動
^P/^N, ↑/↓  down-line-or-history             1 行下へ, 先頭行/最終行 にいるときは履歴を移動
            up-history
            down-history
            vi-up-line-or-history
            vi-down-line-or-history
            beginning-of-buffer-or-history   の先頭へ, すでにそこにいるときは履歴を移動
            end-of-buffer-or-history         の末尾へ, すでにそこにいるときは履歴を移動
M-< / M->   beginning-of-history             最初・最後の履歴へ
M-< / M->   end-of-history                   最初・最後の履歴へ
```


## 補足

- `.forward-char` のように頭に `.` が付く名前は, 組み込 前の widgetを自分で再定義していても,  
  こちらは常に元の動作を呼び出します
- 次の widget は標準では読み込まれていない追加の関数 zle -N <名前> で読み込むと使えます
  - `up-line-or-beginning-search / down-line-or-beginning-search` : 入力済みの文字列から始まる履歴をたどって上下移動
  - `forward-word-match / backward-word-match` : 単語のれる単語移動
- ex
  ```
  bindkey '^[[1;5C' forward-word    # Ctrl-→
  bindkey '^[[1;5D' backward-word   # Ctrl-←
  ```
- 現在の割り当ては bindkey で, 全 widget の list は zle


