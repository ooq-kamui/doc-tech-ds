
# git pull  -  err


## git pull 時に commit conflict のとき

```
remote: Enumerating objects: 9, done.
remote: Counting objects: 100% (9/9), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 5 (delta 1), reused 5 (delta 1), pack-reused 0 (from 0)
Unpacking objects: 100% (5/5), 352 bytes | 88.00 KiB/s, done.
From https://github.com/ooq-kamui/xxx
 * branch            main       -> FETCH_HEAD
   7133307..370968f  main       -> origin/main
fatal: Not possible to fast-forward, aborting.
```

### resolve

```
wip:
```


## git pull 時に err

```
remote: Enumerating objects: 7, done.
remote: Counting objects: 100% (7/7), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 4 (delta 2), reused 4 (delta 2), pack-reused 0 (from 0)
Unpacking objects: 100% (4/4), 370 bytes | 123.00 KiB/s, done.
From https://github.com/ooq-kamui/dotfiles
   b09e01b..ee6bf36  main       -> origin/main
hint: Diverging branches can't be fast-forwarded, you need to either:
hint:
hint:   git merge --no-ff
hint:
hint: or:
hint:
hint:   git rebase
hint:
hint: Disable this message with "git config set advice.diverging false"
fatal: Not possible to fast-forward, aborting.
```

### resolve

```
wip:
```



