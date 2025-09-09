
# vim fnc ( built in )


## ref

https://vim-jp.org/vimdoc-ja/builtin.html#builtin-function-list


## fnc ( built in )

### match

```
match({expr}, {pat} [, {start} [, {count}]])
数値:  {expr}内で{pat}がマッチする位置

matchend({expr}, {pat} [, {start} [, {count}]])
数値:  {expr}内で{pat}が終了する位置

matchstr({expr}, {pat} [, {start} [, {count}]])
文字列:  {expr}内の{count}番目の{pat}のマッチ
```


### string

```
nr2char()         数値から文字を得る
list2str()        数値のリストから文字列を得る

char2nr()         文字の数値を得る
str2list()        文字列から数値のリストを得る
str2nr()          文字列を数値に変換する
str2float()       文字列を浮動小数点数に変換する

printf()          書式付き文字列を整形する

tr()              ある文字の集合から別の文字の集合へ置換する

strtrans()        文字列を印字可能な状態とする
keytrans()        内部キーコードから :map で使用可能な表記にする

tolower()         文字列を小文字にする
toupper()         文字列を大文字にする

charclass()       文字のクラス

match()           文字列の中でパターンにマッチした位置
matchbufline()    バッファ内のパターンのすべてのマッチ
matchend()        文字列の中でパターンにマッチした末尾の位置

matchfuzzy()      リスト内の文字列についてファジーマッチした文字列
matchfuzzypos()   リスト内の文字列についてファジーマッチした文字列

matchstr()        文字列の中でパターンにマッチした文字列
matchlist()       matchstr()と同様だが, 部分マッチも返す

matchstrlist()    文字列のリスト内のパターンにマッチするすべての文字列
matchstrpos()     文字列の中でパターンにマッチした文字列と位置

stridx()          文字列の中で部分文字列が見つかった最初の位置
strridx()         文字列の中で部分文字列が見つかった最後の位置

strlen()          文字列のバイト単位での長さ
strcharlen()      文字列の文字単位での長さ
strchars()        文字列内の文字数

strutf16len()     文字列内の UTF-16 コード単位の数

reverse()         文字列内の文字の順序を逆にする

substitute()      パターンにマッチする文字列を置換
submatch()        ":s" と substitute() の中で部分マッチを得る
strpart()         文字列の一部分を得る(バイト数指定)
strcharpart()     str の idx , len で指定された部分文字列を得る

slice()           Vim9 script での文字インデックスを用いて, 文字列のスライスを取る

strgetchar()      文字のインデックスで指定された文字コードを得る

expand()          特殊キーワードを展開する
expandcmd()       `:edit` のようにコマンドを展開する

iconv()           テキストのエンコーディングを変換する

byteidx()         文字列中の文字のバイトインデックス
byteidxcomp()     byteidx() と同様だが合成文字を数に入れる

charidx()         文字列中のバイト値の文字インデックス
utf16idx()        文字列内のバイトの UTF-16 インデックス

repeat()          文字列を複数回繰り返す

eval()            文字列を式として評価する

execute()         Ex コマンドを実行し出力を得る
win_execute()     execute() に似ているが指定ウィンドウで実行する

trim()            文字列から文字を取り除く

gettext()         翻訳メッセージの検索



strwidth()        表示された文字列のサイズ
strdisplaywidth() 表示された文字列のサイズ, タブを扱う

setcellwidths()   文字の幅の上書き設定
getcellwidths()   文字の幅の上書き設定値を取得する

```

escape 関連

```
escape(str, chars)  文字列 {str} 内の {chars} を `\` で escape
shellescape(str)    文字列 {str} をシェルコマンド引数として使うためにエスケープする

fnameescape()       Vim コマンド用にファイル名をエスケープ
```



