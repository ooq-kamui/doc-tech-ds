
# git rebase

ref

https://qiita.com/C_HERO/items/06669621a1eb12d8799e


## basic

派生 branch の 分岐点の commit を 元 branch の 先端 に付け替える

wip:

```
git rebase ???
```


### image

```
dev  : c1 - c2 - c5 - c6
              \
feat :         - c3 - c4

       git rebase

dev  : c1 - c2 - c5 - c6
                        \
feat :                   - c3' - c4'

       c3 c4 はなくなる
```

### q

- conflict してたらどうなるのか
- stash するのと何が違うのか


## notice

`git rebase` は 自分だけが扱う branch でしか行わない こと


## option

```
-i  --interactive
```


## 補足

```
git fetch
```

```
git rebase
```

と

```
git pull --rebase
```

は同じ

notice: 上記は大雑把 


