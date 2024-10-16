
# fzf-vim


## notice

`:Files` では ptn を引数で与えることはできない, dir のみ,
( dir も err になる気がするけど.. )


## vim command

```
:Files [PATH]    Files (similar to :FZF)
:GFiles [OPTS]   Git files (git ls-files)
:GFiles?         Git files (git status)
:Buffers         Open buffers
:Colors          Color schemes
:Ag [PATTERN]    ag search result (ALT-A to select all, ALT-D to deselect all)
:Lines [QUERY]   Lines in loaded buffers
:BLines [QUERY]  Lines in the current buffer
:Tags [QUERY]    Tags in the project (ctags -R)
:BTags [QUERY]   Tags in the current buffer
:Marks           Marks
:Windows         Windows
:Locate PATTERN  locate command output
:History         v:oldfiles and open buffers
:History:        Command history
:History/        Search history
:Snippets        Snippets (UltiSnips)
:Commits         Git commits (requires fugitive.vim)
:BCommits        Git commits for the current buffer
:Commands        Commands
:Maps            Normal mode mappings
:Helptags        Help tags
:Filetypes       File types
```


## filter word 入力中の key bind

```
ctl-t : 新規タブで開く

ctl-f : forward-char          cursor mv char forward
ctl-b : backward-char         cursor mv char back
alt-f : forward-word          cursor mv word forward
alt-b : backward-word         cursor mv word back
ctl-a : beginning-of-line     cursor mv line top
ctl-e : end-of-line           cursor mv line end

ctl-d : delete-char           del char forward
ctl-h : backward-delete-char  del char back
alt-d : kill-word             del word forward
ctl-w : unix-word-rubout      del word back
ctl-u : unix-line-discard     del cursor pos - line top

ctl-l : forward-char          ??
ctl-f : forward-word          ??
```


## 参考

terminal command の fzf の,
filter word 入力中の, key-bind 設定 方法

```
set -x FZF_DEFAULT_OPTS '--bind=ctrl-o:accept'
```



