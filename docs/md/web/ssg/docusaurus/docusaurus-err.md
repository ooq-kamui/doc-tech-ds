
# docusaurus  -  err


## 謎の link 不正エラーが出た場合

とりあえず,
markdown file すべてに対して 空行 1行追加

で, 再 build で直る

詳細不明


## docusaurus の dir を cp 後, `npm run build` で err になる場合

これは node.js の話

node_module 入れ直しをする

node.js の prj dir にて

```
rm -rf node_modules
```

```
npm install
```

err 解消されたか 確認

```
npm run build
```



