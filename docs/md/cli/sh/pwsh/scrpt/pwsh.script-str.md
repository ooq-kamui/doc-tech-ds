
# str


## str 連結

```
$str03 = $str01 + $str02
```


## 文字列の数字 を 数値 に 変換

```
[int] $num_str
```


## 数値 を 文字列 に 変換

```
[string] $num
```


## padding

```
"1".PadLeft(3, '0')
```


## trim

```
$str.Trim()
```


## div ( 分割 )

```
$str = "22:20:10"
$str.Split(':')
```


## 文字列の中で改行

```
$str  = 'aaa' + "`r`n"
$str += 'bbb' + "`r`n"

echo $str
```


## 文字列の 末尾の文字列 の判定

```
if ($str.EndWith('.json')){
  echo 'true'
}
```


