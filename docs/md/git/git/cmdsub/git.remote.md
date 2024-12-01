
# git remote


## local と remote を紐付ける

### 初回設定

```
git remote add origin https://github.com/ooq-kamui/cnf
```

origin はいったん決め打ちのようなものとしておく


token 付き

```
git remote add origin https://access-token@github.com/ooq-kamui/doc-tech-ds
```


### 変更

```
git remote set-url origin https://github.com/ooq-kamui/cnf
```


## 確認

```
git remote -v
```



