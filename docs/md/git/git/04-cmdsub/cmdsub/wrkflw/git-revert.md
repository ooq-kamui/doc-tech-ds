
# git revert


## 概要

- commit を取り消す 新しい commit を作成する


## basic

```
git revert <commit-id>
```


### file の conflict がなかった場合は,  

commit message を入力して, 終わり


### file の conflict が発生した場合は,  

revert 中断 の状態になる

conflict 解消後,

```
git revert --continue
```

で続きの処理がされ,  
完了する


