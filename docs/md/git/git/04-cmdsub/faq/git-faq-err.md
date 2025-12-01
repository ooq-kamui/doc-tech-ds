
# git faq err


## commit の conflict のある状態で, git push した とき

```
[main ↑1] ji push origin main
To https://github.com/ooq-kamui/dotfiles
 ! [rejected]        main -> main (fetch first)
error: failed to push some refs to 'https://github.com/ooq-kamui/dotfiles'
hint: Updates were rejected because the remote contains work that you do not
hint: have locally. This is usually caused by another repository pushing to
hint: the same ref. If you want to integrate the remote changes, use
hint: 'git pull' before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
```

- remote に 未取り込み の commit がある のに push しようとした とき
  - git prompt が `<>` のときなので, 実行前にきづける はず
- このまま git pull すると, 挙動は config の  
  `pull.rebase`  
  `pull.ff`  
  など に従う  
  設定によっては 自動で ( 勝手に ) 新 commit ができてしまう ので注意
- `git pull --rebase origin/<branch-name>` とすれば,  
  pull 時の merge が merge ではなく rebase になる
- err が出た時点で fetch できているので  
- `git rebase origin/<branch-name>` でも同じ ( たぶん )


### resolve

```
git pull --rebase

git push origin main
```


## commit の conflict のある状態で, git pull した とき

```
[main ↑1] git pull
remote: Enumerating objects: 7, done.
remote: Counting objects: 100% (7/7), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 4 (delta 2), reused 4 (delta 2), pack-reused 0 (from 0)
Unpacking objects: 100% (4/4), 353 bytes | 20.00 KiB/s, done.
From https://github.com/ooq-kamui/dotfiles
   edb82d5..8bce649  main       -> origin/main
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
git pull --rebase
```


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





