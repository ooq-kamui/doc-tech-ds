
# git remote


## local と remote を紐付ける

### 初回設定

```
git remote add origin https://github.com/ooq-kamui/cnf
```

origin はいったん決め打ちのようなものとしておく


token 付き

```
git remote add origin https://<access-token>@github.com/ooq-kamui/doc-tech-ds
```


### 変更

```
git remote set-url origin https://github.com/ooq-kamui/cnf
```


## 確認 表示

### 基本

```
git remote -v
```


### remote branch を表示

```
git remote show origin
```


## remote に存在しなくなった branch の local の remote 追跡 branch を del

### 対象 branch を表示

```
git remote prune --dry-run origin
```

### 削除 実行

```
git remote prune origin
```


