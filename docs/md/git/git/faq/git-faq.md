
# faq


## git push 時に rejected

### case

```
To https://github.com/ooq-kamui/dotfiles
 ! [rejected]        main -> main (fetch first)
error: failed to push some refs to 'https://github.com/ooq-kamui/dotfiles'
hint: Updates were rejected because the remote contains work that you do not
hint: have locally. This is usually caused by another repository pushing to
hint: the same ref. If you want to integrate the remote changes, use
hint: 'git pull' before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
```

- このまま git pull すると 3 way merge ? ( っぽく ) なるので注意
- `git pull --rebase origin main` などとすれば,  
  pull 時の merge が merge ではなく rebase になる


## git pull で 勝手に 3 way merge ぽくなってしまうのを, やめたい

first forward merge 以外のときは err で stop するようにする

```
git config --global pull.ff only
```


## q. branch の 親子 は人が考えているだけで, system 的には 並列 なのか ?

### a.

wip:


## q. nano editor が 立ち上がってしまって, 混乱

### a.

https://www.nano-editor.org/


