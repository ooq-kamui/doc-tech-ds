
# code commit


## pc から git push の設定

code commit の repository はあるとする

branch `main` として記述


### console で iam account の作成, 設定

iam account を作成する

aws code commit の https git 認証情報 を生成, dl する

iam account を group に追加する

group に `code commit full access` を付与する


### local pc で git の設定

```
git init
```

```
git remote add https://..
```

```
git config --local user.name <とりあえず aws と関係ない user name でも可>
```

```
git config --local user.email <とりあえず aws と関係ない email でも可>
```

```
git fetch
```

ここで, user name, pw を訊かれる,
dl した credential を入力する


次を実施
- `git checkout main`
- src の修正
- `git add .`, `git commit -m "etc"`


```
git push origin main
```



