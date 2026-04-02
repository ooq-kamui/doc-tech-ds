
# gemini


## install

```
npm install -g @google/gemini-cli
```


## login

```
gemini login
```


## ssh 接続先で gemini auth

- ブラウザなしモード ( NO_BROWSER ) を使用
  - 必要ないかも
- サーバー側で環境変数を設定して実行します

``` bash
export NO_BROWSER=1
gemini login
```

- ターミナルにURLが表示されるので, 手元のPCのブラウザで そのURLを開く
- ブラウザで認証を完了すると "認証コード ( Authorization Code )" が表示されます


## login 状態などを 一度 clean にしたい

```
rm -rf ~/.gemini/
```



