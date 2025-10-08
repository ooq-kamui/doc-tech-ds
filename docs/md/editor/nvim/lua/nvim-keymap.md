
# keymap


## basic

- `vim.keymap.set()` を使用する

ex

```
vim.keymap.set('n', 'm', v.Cursor.__ins_cr)
```


## visual mode の keymap 設定

いったん, `:lua fnc_name()<cr>` での指定が無難

```
vim.keymap.set('x', 'xx', ':lua v.Xxx.xxx_xxx()<cr>')
```

mode などで場合分け したい場合は,

```
vim.keymap.set('x', 'w', function()
  if v.Mode.is__box() then
    return ':lua v.Slctd.box_width__1()<cr>'
  else
    return ':lua v.Slctd.str_edge_out_char__tgl()<cr>'
  end
end, {expr = bl.t})
```

`{expr = true}` は 選択範囲を復元する opt


