
# tmux

ref

https://qiita.com/vintersnow/items/be4b29652ff665c45198


config file

```
~/.tmux.conf
```


config file reload

```
tmux source-file ~/.tmux.conf
```


## tmux の start


## 新規セッション作成

```
tmux

tmux new new-session
tmux new -s (session名)
```


## session の確認

```
tmux ls
```


アタッチ 

```
tmux a 
tmux a -t (session名)
```


デタッチ

```
<Prefix> + d
```


## prefix

prefix deault

```
ctl-b
```

prefix の変更

```
set -g prefix C-x
```

prefix の確認

```
tmux show-options -g prefix
```


## キー操作基本

```
<Prefix> + ?   キーバインド一覧
<Prefix> + :   コマンドプロンプト
<Prefix> + [   コピーモード
```

セッション操作


セッション名変更

```
tmux rename -t (旧session名) (新session名)
< Prefix > + $
```

## セッションの削除

```
tmux kill-session     
tmux kill-session -t (session名)
tmux kill-server      # 全部kill
```


## セッションの一覧選択

```
< Prefix > + s
```


## ウインドウ操作

```
c    新規ウインドウ作成
w    ウインドウの一覧選択
0-9  指定番号のウインドウへ移動
&    ウインドウの破棄
n    次のウインドウへ移動
p    前のウインドウへ移動
l    以前のウインドウへ移動
'    入力番号のウインドウへ移動
.    入力番号にウインドウ番号を変更
,    ウインドウの名前変更
f    ウインドウの検索
```


## ペイン操作

```
%             左右にペイン分割
"             上下にペイン分割
q             ペイン番号を表示
カーソル      指定方向のペインへ移動  連続押しでプレフィックス継続
Ctr-カーソル  ペインのサイズを変更    連続押しでプレフィックス継続
!             ペインを解除してウインドウ化
x             ペインの破棄
o             ペインを順に移動
;             以前のペインへ移動
z             現在のペインを最大化/復帰
スペース      レイアウトを変更
Alt-1-5       レイウトを変更
{             ペインの入れ替え(前方向)
}             ペインの入れ替え(後方向)
ctr+o         ペインの入れ替え(全体)
t             ペインに時計を表示
```

```
Ctr-b :resize-pane -U 数字  上ペインのサイズ変更
Ctr-b :resize-pane -D 数字  下ペインのサイズ変更
Ctr-b :resize-pane -L 数字  左ペインのサイズ変更
Ctr-b :resize-pane -R 数字  右ペインのサイズ変更
```


## scroll

copy mode で行う


## copy mode

```
ctr-b [  で copy mode 開始
q で終了
```


```
ctr-b [   コピーモードに入る
c-space   始点確定
c-w       終点確定
ctr-b ]   tmux 上でペースト
```



