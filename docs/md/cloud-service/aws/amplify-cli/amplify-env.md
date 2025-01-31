
# amplify env


## env の list 表示

```
amplify env list
```


## env の 追加

```
amplify env add dev
```

ここで追加しているのは backend

すでに cloud にある env_name は指定できない


## env の 切り替え

```
amplify env checkout env001
```


## env の 詳細情報 表示

```
amplify env get
```


## cloud 上にある env を pull

```
amplify env pull
```


## local での修正を破棄して, cloud の状態に 戻す

対象 env が選択されている状態で

```
amplify env pull --restore
```

or

```
amplify pull
```

上の 2つは 同じ


## env を 追加で pull

```
amplify pull --appId app_id --envName env_name
```


## env の import

```
amplify env import
```

あまり使わない ?


## env の 削除

あまり使わないほうが無難

```
amplify env remove
```



