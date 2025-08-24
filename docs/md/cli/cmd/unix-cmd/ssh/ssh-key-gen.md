
# ssh key gen


## key type

wip:




## ed25519

key gen

```
cd $home\.ssh
```

ex

```
ssh-keygen -t ed25519 -C "ooq.tiki@gmail.com" -f alm_ed25519
```

下記の key ができる

```
alm_ed25519
alm_ed25519.pub
```

key pub set

接続先 svr で

`alm_ed25519.pub` を `~/.ssh` に置く  
`authorized_keys` に リネーム


