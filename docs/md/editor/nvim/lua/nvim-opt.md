
# nvim lua opt


## ex

```
set xxx
  vim.opt.xxx = true

set noxxx
  vim.opt.xxx = false

set xxx=1
  vim.opt.xxx = 1

set xxx=aaa
  vim.opt.xxx = 'aaa'

set xxx+=aaa
  vim.opt.xxx:append {'aaa'}

set xxx-=aaa
  vim.opt.xxx:remove {'aaa'}

set xxx=aaa,bbb
  vim.opt.xxx = {'aaa', 'bbb'}

set xxx=aa:bb,cc:dd
  vim.opt.xxx = {aa = 'bb', cc = 'dd'}

setlocal xxx
  vim.opt_local.xxx = true

autocmd xxx
  vim.api.nvim_create_autocmd({'BufEnter', 'BufWinEnter'}, {
    group    = vim.api.nvim_create_augroup('grp_name', {}),
    pattern  = {'*.c', '*.h'},
    callback = function()
      print('yyy')
    end,
  })

&bomb
  vim.bo.bomb

xxx on
vim.cmd('xxx on')
```


