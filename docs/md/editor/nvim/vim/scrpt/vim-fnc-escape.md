
# vim fnc  -  escape


## `escape()`

### explain

```
escape(str, chars)
  文字列 {str} 内の {chars} を `\` で escape
```

補足

- target char を指定して, `\` で escape する

### ex

```
let l:str = '().$a'
escape(str, str)

\(\)\.\$\a
```


## `shellescape()`

### explain

```
shellescape(str)
  文字列 {str} をシェルコマンド引数として使うために escape する
```

補足

- `\` は `\\` に escape される
- 全体を `'` で囲った文字列とする

### ex

```
let l:str = '().$a \ / | & b c'
shellescape(l:str)

'().$a \\ / | & b c '
```


