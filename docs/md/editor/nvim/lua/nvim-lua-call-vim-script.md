
# lua use vim script


## lua から vim script を run

```
vim.cmd('echo aaa')
```


## set

```
wip:
```


## key map ( noremap )

```
vim.keymap.set('n', 'T', 'k')
```

### key map & fnc call

```
vim.keymap.set('n', 'T', ':call Tst_fnc()<cr>')
```

### key map & expr

```
-- vim.keymap.set('n', '<c-y>', 'xx')
vim.keymap.set('n', '<c-y>', function()
  return vim.fn.Is_cursor_col__line_end() == 1 and
    ':call Cursor__ins_markdown_cr()<cr>' or
    ':call Cursor__mv_line_end()<cr>'
end, {expr = true})
```


## hi

```
vim.api.nvim_set_hl(0, 'IncSearch', {fg = 'lightyellow', bg = '34'})
```


## vim fnc call

```
vim.fn.fnc_name()
```

ex

```
vim.fn.has('mac')
```

user fnc も 同様

```
vim.fn.My_fnc()
```


## boolean

```
vim script    lua
v:true        true
v:false       false
```

### if 文

```
// false と nil は false, それ以外は true
if val
```

### vim script で定義している function の return boolean を lua で見るとき

```
-- val == 1 で見る必要がある ?
-- ないかも ?
-- wip:

if Is_xxx() == 1

```


## command

```
wip:
```


