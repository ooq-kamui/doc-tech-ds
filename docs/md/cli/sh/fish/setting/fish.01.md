
# fish


## install

```
brew install fish
```


## config.fish 再読込

```
source ~/.config/fish/config.fish
```


## key bind

```
~/.config/fish/config.fish
```
に設定

```
http://fish.rubikitch.com/bind/
```


## key bind 確認

```
fish_key_reader

http://fish.rubikitch.com/fish_key_reader/
```


## wildcard

```
?   / 以外の任意の一文字
*   / 以外のゼロ個以上の任意の文字
**  / を含む全ての文字列
```

```
https://www.gfd-dennou.org/member/hiroki/homepage/main009.html
```


## vi mode

```
fish_vi_key_bindings

fish_default_key_bindings
```


## history

history からの実行

```
tile
と打ってから ctl-p
で tile が含まれるコマンド履歴が直近から表示される
ctl-j で実行
```

history から "xxx" を含むものを検索

```
history search --contains "xxx"
```

history から "xxx" を含むものを削除

```
history delete --contains "xxx"
```

下記でもいけるようではある

```
history delete "xxx"
```


## file line count  ( wc -l )

```
count ( cat file_name )
```



