
# key bind default

```
:help index.txt
```

```
https://vim-jp.org/vimdoc-ja/vimindex.html
```


自分が割り当てた key bind を確認する
```
:map
```


## mode normal key default
```
_   N-1 行下の先頭の char へ移動
-   N   行上の先頭の char へ移動
+   次の行の先頭へ移動
<<  indent を調整
;   最後の f, t, F または T を N 回繰り返す
@   レジスタ {a-z} の内容を N 回実行する
,   最後に実行した f, t, F または T コマンドを 逆向きに N 回繰り返す
.   最後の編集を N 回繰り返す
[   角括弧コマンド 開始

]   角括弧コマンド 開始

=   インデントを調整する
==  インデントを調整する

0   カーソルを行頭文字へ移動
b   単語の先頭に戻る
B   単語の先頭に戻る
c   Nmove のテキストを削除し 挿入モードへ移行
d   Nmove のテキストを削除
D   行末まで削除, d$ と同
e   単語の末尾に進む
E   単語の末尾に進む
f   1行の中で 前方へ 1文字検索
F   1行の中で 後方へ 1文字検索
g_  最後の非空白文字へ移動
ge  単語の末尾に戻る
gE  単語の末尾に戻る
gg  先頭行へ移動
gv  前回の選択範囲を再選択する
G   最終行へ移動
h   左へカーソル移動
H   カーソルを画面の上から N 行目に移動
J   行結合 省略時は2行
L   カーソルを画面の下から N 行目に移動
m   カーソル位置に mark {A-Za-z} をセットする
M   カーソルを画面の中央の行に移動
n   検索文字列に移動 次
N   検索文字列に移動 前
o   カーソルの下に新規に行を挿入, 入力モード
O   カーソルの上に新規に行を挿入, 入力モード
p   カーソルの後に[バッファ x の]テキストを回挿入する
P   カーソルの前に[レジスタ x の]テキストを回挿入する
q   入力した文字をレジスタ {0-9a-zA-Z"} に記録する
    記録中の場合は レジスタへの記録を終了
Q   Ex モードに移行する
r   N 文字を {char} で置き換える
R   置換モードに移行 いまある文字を上書き
s   1文字削除して入力モード
S   N 行削除し[レジスタ x に保存], テキストの挿入開始
    cc と同じ
t   t{char} の文字を右方向へ検索
T   T{char} の文字を左方向へ検索
u   undo
U   1行中の最近の変更をすべて取り消す
v   visual mode char
V   visual mode line
w   単語の先頭に進む
W   単語の先頭に進む
Y   1行 yank
yy  1行 yank
z   zコマンドを実行
<tab>   1つ先の jump list に移動
<space> l と同じ
```


## mode normal ctl key default
```
c-[  割り当てなし
c-]  カーソルの下の単語を :ta (ctags) で検索
c-^  N番目のファイルを編集 (:e #Nと同じ)
c-_  割り当てなし
c-@  割り当てなし

c-a  カーソルの下にある数字を1つインクリメント
c-b  スクロール 1画面 上
c-c  今入力しているコマンドや検索をキャンセル
c-d  スクロール 半画面 下
c-e  カーソルを固定して スクロール 下 1行
c-f  スクロール 1画面 下
c-g  今開いているファイル, 行数, 位置を表示
c-h  1つ左に移動 (hと同じ)
c-i  <Tab>と同じ, 1つ先の jump list に移動
c-j  1つ下に移動 (jと同じ)
c-k  割り当てなし
c-l  スクリーンを再描画
c-m  1つ下に移動 (<CR>と同じ)
c-n  1つ下に移動 (jと同じ)
c-o  1つ前の jump list に移動
c-p  1つ上に移動 (kと同じ)
c-q  矩型選択を開始 ctl-v と同じ
c-r  redo
c-s  割り当てなし
c-t  1つ前のタグリストに移動
c-u  スクロール 半画面上 上
c-v  矩形選択を開始
c-w  {char} ウィンドウコマンド
c-x  カーソルの下の数字を１つデクリメント
c-y  カーソルを固定して スクロール 上 1行
c-z  vim を停止, jobs で一覧表示, fg で再開
```


## mode visual default key
```
=  equalprg に設定の外部プログラムで選択範囲をフィルタする
```

##  nomal と同じもの
```
b  単語の先頭に戻る
c  変更
e  単語の末尾に進む
h  noramal と同じ
H  noramal と同じ
i  <> 等で囲む
J  選択範囲の行を連結
L  noramal と同じ
m  noramal と同じ
n  noramal と同じ
N  noramal と同じ
o  選択範囲のもう一方の端に移動する
O  選択範囲のもう一方の端に移動する
r  選択範囲のすべての文字を, 続いて入力する1文字で置き換える
R  選択範囲の行を削除し, 挿入を開始
t  noramal と同じ
T  noramal と同じ
u  小文字に変換
U  大文字に変換
v  visual line 以外 だった場合は visual line に移行
   visual line      だった場合は visual      を終了
w  単語の先頭に進む
x  削除
zf 折りたたむ
zo 折りたたみを展開
>  indent を調整
<  indent を調整
```


## mode visual ctl key default
```
c-c  mode visual の終了
c-f  normal と同じ
c-i  
c-n  normal と同じ
c-p  normal と同じ
c-s  normal と同じ
c-v  visual box 以外 だった場合は visual box に移行
     visual box      だった場合は visual     を終了
```


## mode insert ctl key default
```
c-@  前回のinsert modeで入力した内容を再度入力し、insert modeを抜ける
c-a  前回のinsert modeで入力した内容を再度入力
c-b  割り当てなし
c-c  insert modeを抜ける
c-d  インデントを1段階下げる ( normal modeの < )
c-e  カーソルの下の文字を入力
c-f  割り当てなし
c-g  c-j     insert modeに入った時のカーソル位置の下に移動
c-g  j       insert modeに入った時のカーソル位置の下に移動
c-g  <Down>  insert modeに入った時のカーソル位置の下に移動(未確認)
c-g  c-k     insert modeに入った時のカーソル位置の上に移動
c-g  k       insert modeに入った時のカーソル位置の上に移動
c-g  <Up>    insert modeに入った時のカーソル位置の上に移動(未確認)
c-g  u       undoできない編集を開始(未確認)
c-h  back space
c-i  tab
c-j  改行
c-k  {char} {char}  マルチバイト文字を入力(例:ctl-K ab =「ば」)
c-l  insert modeを抜ける(未確認)
c-m  改行
c-n  カーソルの前にあるキーワードで前方検索し 一致した単語で補完する
c-o  一度だけノーマルモードのコマンドを入力できる
c-p  カーソルの前にあるキーワードで後方検索し 一致した単語で補完する
c-q  ターミナルに登録されていなければ ctl-V と同じ
c-r  {0-9a-z"%#*:=}       レジスタに登録されている文字を貼り付け
c-r  c-r  {0-9a-z"%#*:=}  レジスタに登録されている文字を貼り付け
c-r  c-o  {0-9a-z"%#*:=}  レジスタに登録されている文字を貼り付けてインデントを直さない(未確認)
c-r  c-p  {0-9a-z"%#*:=}  レジスタに登録されている文字を貼り付けてインデントを直す(未確認)
c-s  割り当てなし
c-t  インデントを1段階下げる ( normal mode の > )
c-u  行頭からカーソルの前までを削除
c-v  {a-z}  特殊文字を入力(例:ctl-V a =「^A(アスキーコードが1の文字)」)
c-v  {0-9} {0-9} {0-9}	3バイト文字を入力(例:ctl-V 0 0 1 =「^A(アスキーコードが1の文字)」)
c-w  カーソルの単語の先頭からカーソルの前までを削除
c-x  c-d  定義した識別子を補完
c-x  c-e  1行下にスクロール
c-x  c-f  ファイル名を補完
c-x  c-i  単語を補完
c-x  c-k  辞書から単語を補完
c-x  c-l  行全体を補完
c-x  c-n  次の補完候補を選択
c-x  c-o  omni補完
c-x  c-p  前の補完候補を選択
c-x  c-s  スペルチェック
c-x  c-t  シソーラスから補完
c-x  c-y  1行上にスクロール
c-x  c-u  completefuncから補完
c-x  c-v  コマンドラインモードのように補完
c-x  c-]  タグを補完
c-x  s    スペルチェック
c-y  カーソルの上の単語を入力
c-z  vimを停止
c-[  <esc>と同じ
c-\  c-n  ノーマルモードに移動
c-\  c-g  明示的に insert mode に移動
c-]  短縮入力(Abbreviations)を展開
c-^  lmapを 有効化 無効化
c-_  allowrevinsが設定されている時に言語を切り替える
0 c-d  カーソルの行の全てのインデントを削除
^ c-d  カーソルの行の全てのインデントを削除
```


## mode cmd key default
```
c-b     移動 行頭
c-e     移動 行末
s-right 移動 単語 forward
s-left  移動 単語 back

c-u     削除      カーソル back
c-w     削除 単語 カーソル back

c-p     履歴 back
c-n     履歴 forward

c-f     コマンドラインウィンドウを開く

c-r + レジスタ名
        レジスタの内容を挿入する
```




```
https://vim-jp.org/vimdoc-ja/vimindex.html#ex-edit-index
```


```
c-a  カーソル直前の文字を補完し, すべての候補を挿入
c-b  カーソルをコマンドラインの先頭へ移動
c-c  <esc> と同じ
c-d  カーソル直前の文字に一致する補完候補を一覧表示
c-e  カーソルをコマンドラインの末尾へ移動
c-f  'cedit' が標準設定なら、コマンドラインウィンドウを開く
     そうでないなら未使用
c-g  'incsearch' がアクティブならば、次マッチへ移動
c-h  <bs>  と同じ
c-i  <tab> と同じ
c-j  <cr>  と同じ
c-k  {char1}  {char2} ダイグラフを入力
c-l  カーソル直前の文字を補完し、最も長い候補を挿入
c-m  <CR> と同じ
c-n  'wildchar' を使用して複数の補完候補があるとき: 次の補完候補を表示
     その他: 以前のコマンドラインを履歴から呼び出す
c-o  未使用
c-p  'wildchar' を使用して複数の補完候補があるとき:前の補完候補を表示
     その他: 以前のコマンドラインを履歴から呼び出す
c-q  c-v と同じ (端末制御で使用されていなければ)
c-r  {regname}
     カーソル位置のオブジェクトまたはレジスタの内容をキー入力したかのように挿入
c-r c-r  {regname}
c-r c-o  {regname} カーソル位置のオブジェクトまたはレジスタの内容を文字通りに挿入
c-s  (端末制御に使用)
c-t  'incsearch' がアクティブならば、前マッチへ移動
c-u  すべての文字を削除
c-v  続いて入力する、数字以外の文字をそのまま挿入もしくは3桁の10進数で1バイト文字を指定して挿入
c-w  カーソルより前にある単語を削除
c-x  未使用 (補完機能のために予約)
c-y  モードレス選択をコピー(ヤンク)する
c-z  未使用 (サスペンド機能のために予約)

c-[        <Esc> と同じ
c-\ ctrl-n コマンドラインを破棄して、ノーマルモードへ移行
c-\ ctrl-g コマンドラインを破棄して、'insertmode'に合わせたモードへ移行
c-\ a - d  将来の拡張のために予約
c-\ e      {expr} コマンドラインを{expr}の結果で置き換える
c-^        マップ:lmapの有効無効を切り替える
c-_        'allowrevins' がオンのとき、言語を切り替える (ヘブライ語、ペルシア語)

'wildchar'  カーソル直前の文字を補完する('wildchar' は標準設定なら<Tab>)
<BS>        カーソル直前の文字を削除
{char1} <BS> {char2} 'digraph' がオンの時、ダイグラフを入力する
<tab>       'wildchar' が <Tab> の時: カーソル直前の文字を補完する
<s-tab>     CTL-P と同じ
<nl>        <CR> と同じ
<cr>        入力したコマンドを実行
<esc>       コマンドラインを実行せずに破棄する
<del>       カーソル位置の文字を削除
<left>      カーソルを左へ移動
<s-left>    カーソルを1単語左へ移動
<c-left>    カーソルを1単語左へ移動
<right>     カーソルを右へ移動
<s-right>   カーソルを1単語右へ移動
<c-right>   カーソルを1単語右へ移動
<up>        ヒストリの中でカーソルより前のパターンに一致する1つ前のコマンドラインを呼び出す
<s-up>      ヒストリから1つ前のコマンドラインを呼び出す
<down>      ヒストリの中でカーソルより前のパターンに一致する1つ次のコマンドラインを呼び出す
<s-down>    ヒストリから1つ次のコマンドラインを呼び出す
<home>      カーソルをコマンドラインの先頭へ移動
<end>       カーソルをコマンドラインの末尾へ移動
<pagedown>  <S-Down> と同じ
<pageup>    <S-Up> と同じ
<insert>    挿入モード/置換モードを変更
<leftmouse> カーソルをマウスクリック位置へ移動
```


## operation


## text object
```
aw, iw  wordを選択
aW, iW  WORDを選択
as, is  “sentence” (文)  を選択
ap, ip  “paragraph”(段落)を選択
gn      最後に使われた検索パターンを前方/後方検索してマッチを選択

ab, a(, a), ib i(, i) (,)ブロック，またはその内部を選択
aB, a{, a}, iB i{, i} {,}ブロック，またはその内部を選択
a[, a], i[, i]  [,]ブロック，      またはその内部を選択
a<, a>, i<, i>  <,>ブロック，      またはその内部を選択
a", a', a`, i", i', i`             前の引用符から次の引用符まで, またはその内部を選択
```











