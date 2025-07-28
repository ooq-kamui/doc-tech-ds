
# amplify gen2

一般的な gen2 構築手順


## 手順

### prj dir を `vite + react` で作成

```
npm create vite@latest <prj-dir-name>
```

```
cd <prj-dir-name>
```

```
npm install
```

### browser で確認

```
npm run dev
```

`http://localhost:5173/` で確認


### prj dir を amplify 化する

```
npm create amplify@latest
```

backend の module を追加

```
npm add --save-dev @aws-amplify/backend@latest @aws-amplify/backend-cli@latest typescript
```

amplify ui の module を追加

```
npm add @aws-amplify/ui-react
```

いったん, backend の設定を, 何もなし にする  
( 最低限レベルの確認のため )

vi で 下記を編集

```
vi amplify/backend.ts
```

下記の箇所を, 下記のようにコメントアウト

```
defineBackend({
  // auth,
  // data,
});
```

再度,
`npm run dev` & `http://localhost:5173/` で local の表示を確認


### git の設定

github 等, remote repository を作成

local を 上記の git remote と紐づける

```
git init
```

```
git remote add <url>
```

push する

```
git push origin main
```


### amplify の設定 ( console )

amplify を console から作成

deploy が走るが, 1回目は node-js の ver の問題で err 終了する ( はず )

amplify の build の設定から, node-js の ver を設定する ( とりあえず 22.11 くらい )

再度 deploy する

deploy された main にアクセスしてみる

vite + react の初期画面が表示されれば ok


さきほど 外した,  
backend の `auth` `data` の 呼び出しを もとに戻して, 有効にする

```
vi amplify/backend.ts
```

で編集して, コメントアウトを外す

```
defineBackend({
  auth,
  data,
});

```

### sandbox の設定

```
npx ampx sandbox
```

sandbox の deploy が終わるのを確認  
amplify の console の sandbox から deploy が終わったかを確認できる


### auth の設定

https://qiita.com/moritalous/items/76a05676a564960ac974  
を参考に, 次を編集

- src/main.tsx

```
wip:
```

- src/App.tsx
  - ` signOut, user ` 部分は comment out しないと build で err になる

```
wip:
```


`http://localhost:5173/` にアクセスして確認


push, して deploy する

main にアクセスして, 確認,

表示されていれば ok



