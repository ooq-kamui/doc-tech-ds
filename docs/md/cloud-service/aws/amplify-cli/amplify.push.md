
# amplify push


local の backend resource を cloud に provisioning & deploy する


## 基本

```
amplify push
```


## resource を指定して amplify push

```
amplify push function fnc_name
```


## ref & question

```
amplify status  # local resource の変更を表示する
                # push されていない resource の確認

amplify push    # local の backend         resource を cloud に provisioning & deploy

amplify publish # local の backend & front resource を cloud に provisioning & deploy
```



## question

q. push 先の紐づきはどこで設定しているか ?

a. amplify pull の 初回実行で 設定



