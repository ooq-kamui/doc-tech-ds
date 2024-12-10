
# faq


## 謎の link 不正エラーが出た場合

とりあえず,
markdown file すべてに対して 空行 1行追加

で, 再 build で直る

詳細不明


## `npm run build` で err

docusaurus の dir を cp 後, や,  
docusaurus の git を clone 後  
に err になる場合

これは node.js の話

node_module 入れ直しをする

node.js の prj dir にて

```
rm -rf node_modules
```

```
npm install
```

で必要な module が re install される

err 解消されたか 確認

```
npm run build
```



