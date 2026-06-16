
# osc52

ssh 接続先 から local pc に clipboard copy する


## src

https://chromium.googlesource.com/apps/libapps/+/master/hterm/etc


## install

### sh

```
wip:
```


### vim

.vimrc

ex

```
source ~/xxx/osc52.vim
vmap <C-c> y:call SendViaOSC52(getreg('"'))<cr>
```



