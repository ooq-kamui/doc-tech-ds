
# ssh key gen


## pwsh

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


## key pub set

接続先 svr で

`alm_ed25519.pub` を `~/.ssh` において  
`authorized_keys` に リネーム


