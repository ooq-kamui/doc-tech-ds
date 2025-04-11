
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
vim.keymap.set('n', 'T', '<cmd>call Tst_fnc()<cr>')
```

### key map & expr

```
wip:

nnoremap <expr> <c-y>
```


## hi

```
wip:
```


## command

```
wip:
```


## vim fnc call

```
vim.fn.fnc_name()
```

ex

```
vim.fn.has('mac')
```

user def fnc も 呼べます

```
vim.fn.My_fnc()
```


