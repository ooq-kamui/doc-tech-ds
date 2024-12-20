
# ptn regex


## ref

https://qiita.com/kawaz/items/d0708a4ab08e572f38f3


```

繰返し制御系（量指定子）

a*  は0回以上の a の繰り返しにマッチする。（最長一致）
a+  は単に a+ という文字列にマッチする。
a\+ は1回以上の a の繰り返しにマッチする。（最長一致）
a?  は単に a? という文字列にマッチする。
a\? は0または1個の a にマッチする。
a\= は0または1個の a にマッチする。（\? と基本同じだが \? は後方検索で使えない）

a\{n,m} 系（『pregのa{n,m}系』と基本同じ、どれも最長一致）

a\{n}   は 丁度 n 回の a の繰り返しにマッチする。
a\{n,}  は n回以上の a の繰り返しにマッチする。（最長マッチ）
a\{1,}  は 1 回以上 a の繰り返しにマッチする。（最長マッチ、a\+ と同じ）
a\{n,m} は n回以上 m 回以下の a の繰り返しにマッチする。（最長マッチ）
a\{,m}  は 0 回以上 m 回以下の a の繰り返しにマッチする。（最長マッチ）
a\{,}   は 0 回以上 a ã®繰り返しにマッチする。（最長マッチ、a* と同じ）
a\{}    は 0 回以上 a の繰り返しにマッチする。（最長マッチ、a* と同じ）

a\{-n,m} 系（a\{n,m} と基本同じだがブレス内の頭に - をつけることで最短一致になる）

a\{-n}   は 丁度 n 回の a の繰り返しにマッチする。（-のアリナシで意味に違いはない）
a\{-n,}  は n 回以上の a の繰り返しにマッチする。（最短マッチ、『pregのa{n,}?と同じ』））
a\{-1,}  は 1 回以上 a の繰り返しにマッチする。（最短マッチ、『pregのa+?』と同じ）
a\{-n,m} は n 回以上 m 回以下の a の繰り返しにマッチする。（最短マッチ、『pregのa{n,m}?と同じ』）
a\{-,m}  は 0 回以上 m 回以下の a の繰り返しにマッチする。（最短マッチ、『pregのa{,m}?と同じ』）
a\{-,1}  は 0か1個の a にマッチする。（最短マッチ、『pregのa??』と同じ）
a\{-,}   は 0 回以上 a の繰りè¿しにマッチする。（最短マッチ、『pregのa*?』と同じ）
a\{-}    は 0 回以上 a の繰り返しにマッチする。（最短マッチ、『pregのa*?』と同じ）

\@>      強欲な量指定子。直前のパターンが強欲にマッチするようになる。（『(Perlの(?>pattern)と似ている）
         \(a*\)\@>b は aaab にマッチするが、\(a*\)\@>ab は aaab に決してマッチしない。なぜなら \(a*)\@> が先に aaa まで取ってしまいバックトラックもしないので次の文字は b となり、後が ab になることはないため。


グルーピング系

(foo|bar)     は 単に (foo|bar) という文字列にマッチする。
\(foo\|bar\)  は foo か bar にマッチする。部分正規表現に一致した文字列は、\1 や \2 で後方参照できる。
\%(foo\|bar\) は foo か bar にマッチする。\(foo\|bar\) と基本的に同じだが後方参照を作らないので。その分高速。（『pregの(?:foo|bar)』と同じ）
\z(foo\|bar\) は foo か bar にマッチする。__syntaxコマンドのstart=オプションの中でのみ使用可能__で、部分正規表現に一致した文字列は同コマンドのend=オプションの中で \z1 や \z2 で参照できる。
a\%[bcd]      は a/ab/abc/abcd にマッチする。 ad にはマッチしない。（Perlのa(b(cd?)?)?みたいなイメージ）

文字エスケープ

\e は <Esc> にマッチする。
\t は <Tab> にマッチする。
\r は <CR> にマッチする。
\b は <BS> にマッチする。
\n は 改行文字にマッチする。

文字クラス系

[a-z]  は a,b,c,...,z の文字にマッチする。pregと同じ。
[^a-z] は a,b,c,...,z 以外の文字にマッチする。pregと同じ。

. は改行以外のすべての文字にマッチする。

\s は 改行以外の空白文字にマッチする。
\d は [0-9] と同じ。（10進数に使われる文字）
\x は [0-9A-Fa-f] と同じ。（16進数に使われる文字）
\o は [0-7] と同じ。（8進数に使われる文字）
\w は [0-9A-Za-z_] と同じ。（単語に使われる文字）
\h は [A-Za-z_] と同じ。（\wから数字を除いたもの、単語の先頭文字）
\a は [A-Za-z] と同じ。（英字）
\l は [a-z] と同じ。（英字の小文字）
\u は [A-Z] と同じ。（英字の大文字）

上記以外にマッチ

\S  空白以外の文字 にマッチする。
\D  数字以外の文字 にマッチする。
\X  
\O  
\W  
\H  
\A  
\L  
\U

\_ + 上記 で 改行を含む 上記 にマッチする。

\_. は 改行を含む すべての文字にマッチする。（Perlのs修飾子を付けた状態みたいな感じ）
\_s は 改行を含む 空白文字にマッチする。
\_d は 改行を含む ... にマッチする
\_x は 改行を含む ... にマッチする
\_o は 改行を含む ... にマッチする
\_w は 改行を含む ... にマッチする
\_h は 改行を含む ... にマッチする
\_a は 改行を含む ... にマッチする
\_l は 改行を含む ... にマッチする
\_u は 改行を含む ... にマッチする
\_S は 改行を含む ... にマッチする
\_D は 改行を含む ... にマッチする
\_X は 改行を含む ... にマッチする
\_O は 改行を含む ... にマッチする
\_W は 改行を含む ... にマッチする
\_H は 改行を含む ... にマッチする
\_A は 改行を含む ... にマッチする
\_L は 改行を含む ... にマッチする
\_U は 改行を含む ... にマッチする


\_[a-z]     は 『[a-z]と改行文字』にマッチする。
\%d123      は 10進数で指定した文字にマッチする。（最大値=255）
\%o40       は 8進数で指定した文字にマッチする。(最大値=377=255)
\%x2a       は 16進数で指定した文字にマッチします。(最大値=ff=255)
\%u20AC     は 16進数で指定した文字にマッチする。(4桁まで)
\%U1234abcd は 16進数で指定した文字にマッチします。(8桁まで)

[:alnum:]
[:alpha:]
[:blank:]
[:cntrl:]
[:digit:]
[:graph:]
[:lower:]
[:print:]
[:punct:]
[:space:]
[:upper:]
[:xdigit:]
[:return:]
[:tab:]
[:escape:]
[:backspace:]


位置指定系

位置指定形 は全て幅ゼロでマッチします。

^   と $   は vimでは常に各々行頭と行末にマッチする。
\%^ と \%$ は テキストの先頭と末尾にマッチする。（Perlのm修飾子を付けた状態みたいな感じ）
\<  と \>  は ワードの直前と直後にマッチする。\<var\> は var hoge=1 にマッチするが variable にはマッチしない。

\zs はマッチの開始地点を設定する。これより前は幅ゼロ扱いでマッチに含まない。後読みの代わりに使える。複数マッチした場合は一番最後が有効。
\ze はマッチの終了地点を設定する。これより後は幅ゼロ扱いでマッチに含まない。先読みの代わりに使える。複数マッチした場合は一番最後が有効。

位置指定系（vimの状態や座標に関係するもの）

\%V は ビジュアルモードの範囲内にマッチする。\%Vfoo\%V は選択範囲内の foo にマッチする。\%Vでマッチの前後を挟むのが基本的な使い方になる。
\%# は カーソル位置にマッチする。\k\%#\k はカーソル位置の単語、\s*\%#\s* はカーソル位置の空白文字の連続にマッチする。

\%'m   \%<'m   \%>'m  はそれぞれ、『マークm』の位置、『マークm』の前、『マークm』の後にマッチする。
\%23   \%<23   \%>23  はそれぞれ、23行目の行、23行目より上の行、23行目より下の行にマッチする。
\%23c  \%<23c  \%>23c はそれぞれ、23列目、23列目より前の列、23列目より後の列にマッチする。
\%23v  \%<23v  \%>23v はそれぞれ、23列目の表示列、23列目の表示列より前の列、23列目の表示列より後の列にマッチする。

先読み, 後読み

\@=   肯定先読み。foo\%(bar\)\@= は直後にbarがあるfooにマッチする、bar部分はゼロ幅扱いでマッチに含まない。（『Perlの(?=bar)』と同じ）
                  foo\%(bar\)\@=  は \ze を使って、foo\zebar と書くことも出来る。
\@!   否定先読み。foo\%(bar\)\@! は直後にbarがないfooにマッチする。（『Perlの(?!bar)』と同じ）
                  否定先読みは高コストなので出来るだけ使わないほうが良い。
\@<=  肯定後読み。\%(foo\)\@<=bar は直前にfooがあるbarにマッチする、foo部分はゼロ幅扱いでマッチに含まれない。（『Perlの(?<=pattern)』と基本同じだが、vimでは量指定子も使える）
                  \@123<= とすると \@<= と基本同じだが、パフォーマンスのために遡ってチェックするバイã数を制限できる。
                  \%(foo\)\@<bar は \zs を使って foo\zsbar と書くことも出来る。
                  否定後読みの対象パターンが後方参照を作るとき、正規表現エンジンのバージョンによってその挙動に違いが出ることがあるらしくポータビリティを考えると \zs を使って書いたほうが良いらしい。
\@<!  否定後読み。\%(foo\)\@<!bar は直前にfooがないbarにマッチする。（『Perlの(?<!pattern)』と基本同じだが、vimでは量指定子も使える）
                  \@123<! とすると \@<! と基本同じだが、パフォーマンスのために遡ってチェックするバイト数を制限できる。否定後読みは高コストなので出来るだけ範囲制限をかけるようにした方が良い。


心の声 : vim の先読み後読みの \@XX 系パターンは記号自体がゴツいのとpregと違って記号を後置するのが慣れないので、
         \zs と \ze で代替出来るケースでは後者を使うæ¹が個人的には好みです。
         ただ、他人の書いたコードを読むと \@XX も結構出てくるので読めないと困るのでその確認用にまとめ直しはじめたのがこのエントリです。


修飾子みたいなやつ

\c   をパターンに含めると  パターン全体で大文字と小文字の違いが無視されるようになる。但し \w とかの文字クラスには影響しない。
\C   をパターンに含めると  パターン全体で大文字と小文字の違いが区別されるようになる。但し \w とかの文字クラスには影響しない。

\m, \M, \v, \V はそれ以降パターンを magic, nomagic, very magic, very nomagic 状態にする。


合成文字関連（詳細は各自でドキュメント確認して…）

\Z   をパターンに含めるとパターン全体で合成文字が無視される。
     càt という文字列に対して、cat ではマッチしないが \Zcat や cat\Z とするとマッチできる。

\%C  は直前のパタã¼ンについてのみ合成文字を無視する。
     aà aa àà という文字列に対して、aa\%C は aà や aa の部分にはマッチするが àà にはマッチしない。


その他

~ は最後に置換された文字列にマッチする。
```


