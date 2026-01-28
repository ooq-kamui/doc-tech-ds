
# git branch


## notice

いまどきは branch の作成削除などは github 上でやるのが  
一般的で無難だと思います

ということで, 自分としては  
git branch は branch の状態を見る のがメインのコマンドとしてとらえます


## local branch の list を表示

```
git branch
```


## local branch の list を表示, で HEAD commit 情報 もつける

```
git branch -v
```


## upstream branch

### 確認

`git config --local --list` で次の値

```
branch.<local-branch-name>.remote=origin
branch.<local-branch-name>.merge=refs/heads/<remote-branch-name>
```

- 通常は local branch と同じ branch

ex

```
branch.main.remote=origin
branch.main.merge=refs/heads/main
```


### 設定

```
git branch --set-upstream-to=origin/<remote-branch-name> <local-branch-name>
```

ex

```
git branch --set-upstream-to=origin/main main
```

```
branch.main.remote=origin
branch.main.merge=refs/heads/main
```


## 下記は何を示しているか, は調査中

```
git branch -vv
```


## remote tracking branch の list を表示

```
git branch -r
```


## local branch と remote tracking branch の list を表示

```
git branch -a
```


---

## branch を切り替える

branch の切り替えは `checkout` または `switch`

```
git checkout <branch-name>
```

or

```
git switch <branch-name>
```


---

通常, github などの remote はあるはずなので,  
branch の操作は github などからやるのが無難です


## branch を作成

```
git branch <branch-name>
```


## branch name を変更する

```
git branch -m name_old name_new
```

ex

```
git branch -m master main
```


## local branch を削除

```
git branch -d <branch-name>
```

- `<branch-name>` が push 済 の場合 local を削除する


## remote branch が削除されたのに合わせて, local branch も削除する

remote で 削除された local の remote tracking branch を 削除

```
git fetch --prune
```

local branch は 個別に削除

```
git branch -d <branch-name>
```


## branch 強制削除

`<branch-name>` が push 済 でないが, 強制削除したいとき

```
git branch -D <branch-name>
```


## branch remote を削除

```
git push origin --delete <branch-name>
```


