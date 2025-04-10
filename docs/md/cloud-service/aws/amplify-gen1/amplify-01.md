
# はじめての amplify cli


## install

```
npm install -g @aws-amplify/cli
```

ref

https://qiita.com/Toyoizumi-Hiroyuki/items/64e89a12f2c004d75194


はじめに,
`amplify configure` で user ( iam ) setting してから 使う

[`amplify configure`](amplify.configure.md )



## 基本的な subcmd

```
amplify configure        # user ( iam ) を追加するなど
                         
amplify init             # init backend
                         #   amplify/ src/ が作成される


amplify add              # app で使用する機能を追加
                         
amplify update           # app で使用する機能を 更新


amplify env list         # 環境の 確認

amplify env add dev      # 環境の 追加

amplify env checkout dev # 環境の 切り替え

amplify env get          # 環境の 詳細情報 表示


amplify pull             # cloud の src を pull する
                         # 初回実行で 紐づき先の prj env を設定できる

amplify status           # 状態を確認
                         # aws cloud に push されていない local resource の状態を 表示する
                         # ( git status に似ている ? )

amplify push             # local の backend         resource を cloud に provisioning
                         #   deploy しているか不明

amplify publish          # local の backend & front resource を cloud に provisioning & deploy
                         #   厳密にはちょっと違うかも ?


amplify api              # api resource の操作 

amplify function         # function resouce の操作


amplify mock             # local で test

amplify mock api         # local で test, api



amplify console

amplify console api

amplify delete           # cloud resource をすべて削除

amplify help             # help
```


## amplify add xxx で 追加可能な aws resource

```
api           : api gateway ( rest ), app sync ( graphql )

auth          : cognito

storage       : s3, dynamo db

function      : lambda

analytics     : pinpoint

hosting       : s3, cloud front distribution

notifications : pinpoint

interactions  : lex
```

ex

```
amplify add api               # api を作成
```

```
amplify add hosting           # deploy method select
```


## ref

https://qiita.com/bonjiko/items/93e8fad618bd4b588b63



