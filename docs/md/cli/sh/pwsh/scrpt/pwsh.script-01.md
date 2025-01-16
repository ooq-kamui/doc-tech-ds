
# pwsh script


## lang spc

https://learn.microsoft.com/ja-jp/powershell/scripting/lang-spec/chapter-01?view=powershell-7.5


## comment

```
# comment
```


## fnc

```
```


### fnc args

可変長引数は `param()` を使わないで, `$args` を使う

```
function fnc(){

  # param($p1, $p2)

  echo $args
}
```


## 改行を無視

バックゥォート を 行末に書く

ex

```
echo "aa   `
bb   "
```



