
# lua str srch ptn


## find ( srch idx )

```
string.find(str, pattern, init, plain)

str      str
pattern  str or regexp-obj
         文字列の regexp でも可 ( 要確認 )
s_idx    int
plain    bool

str の先頭から, pattern に match する部分を探し,
  match する部分が見つかった   場合
    match する部分の start idx, end idx を返す
    str の 1文字目 を idx = 1 とする

  match する部分が見つからない 場合
    nil を返す

pattern が キャプチャ を持っている場合には,
  3番目 以降の戻り値 で, キャプチャされた文字列 を返す
  複数ある場合には, 列挙 ですべて返します ( 要確認 )

s_idx を指定した場合,
  pattern を探し始める場所を先頭ではなく,
  s_idx 文字目 から始めることができます

  s_idx に負の数を指定した場合,
    末尾から何文字目, という 開始位置 となります

plain に true を指定した場合,
  pattern は 単なる 文字列 と解釈されます

  pattern が regexp-obj かつ plain が true の場合,
    nil を返します

a, b = string.find("ABCDE", "BC"  )      -- a=2, b=3
a, b = string.find("ABCDE", "%a*" )      -- a=1, b=5
a, b = string.find("ABCDE", /\a*/ )      -- a=1, b=5

a, b = string.find("あいうえお", "いう") -- a=3, b=6

a, b, c = string.find("ABCDE", "B(.)D")  -- a=2, b=4, c="C"
```


## match ( ptn )

```
string.match(str, pattern, s_idx)

str      str
pattern  str or regexp-obj
         文字列の regexp でも可 ( 要確認 )
s_idx    int

str から pattern に match する部分を 先頭から探し,
  pattern に match する部分が ある 場合
    pattern に キャプチャ が ない 場合
      pattern に match する文字列 を返す

    pattern に キャプチャ が ある 場合
      キャプチャ を 返す
        複数あるときは, 列挙 で返す ( 要確認 )

  pattern に match する部分が ない 場合
    nil を返す

s_idx を指定した場合,
  pattern は str の s_idx 文字目から探し始めます
  省略した場合は 1文字目 からとなります
  s_idx には負の数も指定できまる
    その場合は末尾から何文字目, という形になります

pattern が regexp-obj で,
  オプションとして g が指定されているとき,
  文字列中に見つかった部分で,
  重複していないものをすべて返します
  その他の場合には, 最初に見つかった部分だけを返します

ex

x = string.match("hello world", "%w+"   )
-- x = "hello"

x = string.match("hello world", " (%w+)")
-- x = "world"

x = string.match("hello world", "%w+", 2)
-- x = "ello"

x,y,z,w = string.match("hello world", /\w\w/g)
-- x = "he", y = "ll", z = "wo", w = "rl"

x = {string.match("hello world", /\w\w/g)}
-- x = { "he", "ll", "wo", "rl" }

```


## 文字列の分割

```
> s = "hello world from Lua"
> for w in s:gmatch("%a+") do
>>   print(w)
>> end
hello
world
from
Lua
```


