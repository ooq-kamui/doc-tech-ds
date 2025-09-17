
# git push  -  err


## rejected

```
To https://github.com/ooq-kamui/dotfiles
 ! [rejected]        main -> main (fetch first)
error: failed to push some refs to 'https://github.com/ooq-kamui/xxx'
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




