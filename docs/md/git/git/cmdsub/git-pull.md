
# git pull


## 基本

git pull は, 次の コマンドを一度にやることです

```
git fetch origin main

git merge FETCH_HEAD
```

補足

```
FETCH_HEAD : fetch した remote の 同 branch の 最新 commit
```



## git pull -f ( 強制 ) はありません

そのようなときは, 次のコマンドを実行します

remote 最新を取得

```
git fetch origin main
```

local main を remote の main に強制的に合わせる

```
git reset --hard origin/main
```


`git push -f` で強制的に remote を変更したあと,
別の local で上記を行う ことになる


## q

### local の現在の branch と pull で指定した branch が違うとどうなる?



