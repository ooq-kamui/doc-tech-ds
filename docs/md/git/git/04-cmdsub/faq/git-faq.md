
# faq


## git pull で 自動で ( 勝手に ) 新 commit ができる のを やめたい

### first forward merge 以外のときは err で stop するようにする

```
git config --global pull.ff only
```


## branch の 親子 は人がそう考えているだけで, system 的には 並列 なのか ?

### a.

そうです


## nano editor が 立ち上がってしまって, 混乱

### 最低限の操作方法を見るべし

https://www.nano-editor.org/

wip:

余力あるとき, ここにも書く


## fish の cmdline で git status の `=` などが表示されるようにしたい

- remote upstream branch を設定する
  - ex `git branch --set-upstream-to=origin/main main`




