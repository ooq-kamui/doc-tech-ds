
# git cherry-pick


## basic

特定の commit ( だけ ) を取り込む

```
git cherry-pick commit_id
```


## git stash drop の復活

誤って, git stash の data を pop していないのに drop してしまったとき

```
git cherry-pick -n -m1 <hash>
```


