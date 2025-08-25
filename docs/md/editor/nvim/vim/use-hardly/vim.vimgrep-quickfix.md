
# vim vimgrep , quickfix


## vimgrep

```
:vim pattern **/*.lua
```

結果を quickfix で開く  -  自動
```
:vim pattern **/*.lua | cw
```

結果を quickfix で開く  -  手動
```
:vim pattern **/*.lua
:copne
```

次の分割ウィンドウへ移動
```
<c-w>w
```


## :grep  -  外部grep
```
:grep pattern **/*.lua
```


## vimgrep

さらに絞り込み  quickfix
```
:Cfilter /{pat}/
```

match しない行を残す
```
:Cfilter! /{pat}/
```

さらに絞り込み  location list
```
:Lfilter /{pat}/
```










