
# vim cmd  -  usr def


## args

### official doc explain

```
<args>   : 与えられた通りのコマンド引数

<f-args> : 関数の引数として渡せるように
           引数を空白で区切ったものを
           それぞれをクォートしてカンマで区切ったものに展開します
           実際のルールはもう少し複雑です
           詳細は :help <f-args> を参照してください

<q-args> : 式の文字列として扱えるようにクォートされます
           abc  > "abc"
           a"bc > "a\"bc"
           引数がない場合は空文字列になります
```

### i think ..

```
<q-args> : cmd で 複数 arg でも, 関数には 1 つ の arg になる .. ?
```


## escape

### `shellescape()`

wip:

```
shellescape()
```


### `escape()`

wip:

```
escape()
```



