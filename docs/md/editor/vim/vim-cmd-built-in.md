
# ex cmd  ex-cmd-index :index

以下に すべての : コマンドを列挙した  
引数についての説明はしていない  

コマンド名の省略可能な部分を [] で囲った  
省略できない部分を対象としてソート


```
タグ            コマンド          動作
:               :                 なし
:range          :{range}          {range}の最終行へジャンプ
:!              :!                行をフィルタにかける、または、外部コマンドを実行する
:!!             :!!               最後に実行した ":!" コマンドを繰り返す
:#              :#                ":number" と同じ。
:&              :&                最後に実行した ":substitute" を繰り返す
:star           :*                レジスタの内容を実行する
:<              :<                'shiftwidth' 1つ分だけ行を左へシフト
:=              :=                カーソルのある行の行番号を表示
:>              :>                'shiftwidth' 1つ分だけ行を右へシフト
:@              :@                レジスタの内容を実行
:@@             :@@               直前の ":@" を繰り返す
:Next           :N[ext]           引数リストの1つ前のファイルを編集
:Print          :P[rint]          行を表示する
:X              :X                暗号鍵を設定する
:append         :a[ppend]         テキストを追加する
:abbreviate     :ab[breviate]     短縮入力を登録する
:abclear        :abc[lear]        すべての短縮入力を削除する
:aboveleft      :abo[veleft]      ウィンドウが左もしくは上に分割されるようにする
:all            :al[l]            引数リストの全ファイルをウィンドウ作成して表示
:amenu          :am[enu]          すべてのモードに対してメニュー項目を追加
:anoremenu      :an[oremenu]      すべてのモードに対して再マップされないメニュー項目を追加
:args           :ar[gs]           引数リストを表示
:argadd         :arga[dd]         引数リストにファイルを追加する
:argdelete      :argd[elete]      引数リストからファイルを削除する
:argedit        :arge[dit]        引数リストにファイルを追加し、開く
:argdo          :argdo            引数リストのすべてのファイルに対してコマンドを実行する
:argglobal      :argg[lobal]      グローバル引数リストを使用する
:arglocal       :argl[ocal]       ローカル引数リストを使用する
:argument       :argu[ment]       引数リストの指定したファイルを開く
:ascii          :as[cii]          カーソル位置の文字のASCIIコードを表示
:autocmd        :au[tocmd]        自動コマンドの入力と表示
:augroup        :aug[roup]        使用する自動コマンドグループの選択と表示
:aunmenu        :aun[menu]        すべてのモードに対してメニュー項目を削除
:buffer         :b[uffer]         バッファリストの指定したバッファを開く
:bNext          :bN[ext]          バッファリストの前のバッファを開く
:ball           :ba[ll]           バッファリストのすべてのバッファをウィンドウを作成して開く
:badd           :bad[d]           バッファリストにバッファを追加
:bdelete        :bd[elete]        バッファリストからバッファを削除
:behave         :be[have]         マウス操作や選択の動作を設定する
:belowright     :bel[owright]     ウィンドウが右もしくは下に分割されるようにする
:bfirst         :bf[irst]         バッファリストの最初のバッファを開く
:blast          :bl[ast]          バッファリストの最後のバッファを開く
:bmodified      :bm[odified]      バッファリストの次の変更済みバッファを開く
:bnext          :bn[ext]          バッファリストの次のバッファを開く
:botright       :bo[tright]       ウィンドウが最も右もしくは最も下に分割されるようにする
:bprevious      :bp[revious]      バッファリストの前のバッファを開く
:brewind        :br[ewind]        バッファリストの先頭のバッファを開く
:break          :brea[k]          while ループを抜ける
:breakadd       :breaka[dd]       デバッガのブレークポイントを追加する
:breakdel       :breakd[el]       デバッガのブレークポイントを削除する
:breaklist      :breakl[ist]      デバッガのブレークポイントを一覧表示する
:browse         :bro[wse]         ファイル選択ダイアログをポップアップする
:bufdo          :bufdo            バッファリストのすべてのバッファに対してコマンドを実行する
:buffers        :buffers          バッファリストのファイル名をリスト表示
:bunload        :bun[load]        指定のバッファをアンロード
:bwipeout       :bw[ipeout]       バッファの一切を削除する
:change         :c[hange]         1行または連続する複数行を上書きする
:cNext          :cN[ext]          直前のエラーへジャンプ
:cNfile         :cNf[ile]         エラーリストの前のファイルの最後のエラーへ移動する
:cabbrev        :ca[bbrev]        コマンドラインモードを対象とする ":abbreviate" コマンド
:cabclear       :cabc[lear]       コマンドラインモードにおけるすべての短縮入力を削除
:cabove         :cabo[ve]         現在の行の上のエラーにジャンプ
:caddbuffer     :cad[dbuffer]     バッファからエラーを追加する
:caddexpr       :cadde[xpr]       式からエラーを追加する
:caddfile       :caddf[ile]       現在のQuickFixリストにエラーメッセージを追加
:cafter         :caf[ter]         現在のカーソルの後ろのエラーにジャンプ
:call           :cal[l]           関数を実行する
:catch          :cat[ch]          :tryコマンドの一部
:cbefore        :cbef[ore]        現在のカーソルの前のエラーにジャンプ
:cbelow         :cbel[ow]         現在の行の下のエラーにジャンプ
:cbottom        :cbo[ttom]        QuickFixウィンドウの最下へスクロールする
:cbuffer        :cb[uffer]        エラーメッセージを解釈し、最初のエラーへジャンプ
:cc             :cc               指定のエラーへジャンプ
:cclose         :ccl[ose]         QuickFixウィンドウを閉じる
:cd             :cd               ディレクトリの移動
:cdo            :cdo              QuickFixリストの各項目に対してコマンドを実行する
:cfdo           :cfd[o]           QuickFixリストの各ファイルに対してコマンドを実行する
:center         :ce[nter]         行を中央寄せに整形
:cexpr          :cex[pr]          式からエラーを読みこみ、最初のエラーへジャンプ
:cfile          :cf[ile]          エラーファイルを読み込み最初のエラーへジャンプ
:cfirst         :cfir[st]         指定のエラーへジャンプ。省略時は先頭のエラー
:cgetbuffer     :cgetb[uffer]     バッファからエラーを取得する
:cgetexpr       :cgete[xpr]       式からエラーを取得する
:cgetfile       :cg[etfile]       エラーファイルを読み込む
:changes        :changes          変更リストを表示する
:chdir          :chd[ir]          ディレクトリの移動
:checkpath      :che[ckpath]      インクルードファイルを一覧表示
:checktime      :checkt[ime]      開いているファイルのタイムスタンプを確認する
:chistory       :chi[story]       エラーリストの一覧を表示する
:clast          :cla[st]          指定のエラーへジャンプ、省略時は最後のエラー
:clearjumps     :cle[arjumps]     ジャンプリストを削除する
:clist          :cl[ist]          すべてのエラーを一覧表示
:close          :clo[se]          カレントウィンドウを閉じる
:cmap           :cm[ap]           コマンドラインモードを対象とする":map"コマンド
:cmapclear      :cmapc[lear]      コマンドラインモードのすべてのマップを削除
:cmenu          :cme[nu]          コマンドラインモードのメニューを追加
:cnext          :cn[ext]          次のエラーへジャンプ
:cnewer         :cnew[er]         より新しいエラーリストを使用する
:cnfile         :cnf[ile]         エラーリストの次のファイルの先頭エラーへジャンプ
:cnoremap       :cno[remap]       コマンドラインモードを対象とする ":noremap" コマンド
:cnoreabbrev    :cnorea[bbrev]    コマンドラインモードを対象とする ":noreabbrev" コマンド
:cnoremenu      :cnoreme[nu]      コマンドラインモードを対象とする ":noremenu" コマンド
:copy           :co[py]           行のコピー
:colder         :col[der]         より古いエラーリストを使用する
:colorscheme    :colo[rscheme]    指定した色テーマをロードする
:command        :com[mand]        ユーザー定義コマンドの作成
:comclear       :comc[lear]       すべてのユーザー定義コマンドの削除
:compiler       :comp[iler]       指定したコンパイラ用の設定をする
:continue       :con[tinue]       :while に戻って実行を続ける
:confirm        :conf[irm]        コマンドを実行し、ユーザーの確認が必要ならプロンプトを表示する
:const          :cons[t]          定数として変数を作成する
:copen          :cope[n]          quickfixウィンドウを開く
:cprevious      :cp[revious]      直前のエラーへジャンプ
:cpfile         :cpf[ile]         エラーリストの前のファイルの最後のエラーへジャンプ
:cquit          :cq[uit]          Vimを終了しエラーコードを返す
:crewind        :cr[ewind]        指定のエラーへジャンプ。省略時は先頭のエラー
:cscope         :cs[cope]         cscope コマンドを実行
:cstag          :cst[ag]          cscope を使用してタグへジャンプする
:cunmap         :cu[nmap]         コマンドラインモードを対象とする ":unmap" コマンド
:cunabbrev      :cuna[bbrev]      コマンドラインモードを対象とする ":unabbrev" コマンド
:cunmenu        :cunme[nu]        コマンドラインモードのメニューを削除
:cwindow        :cw[indow]        quickfixウィンドウを開閉する
:delete         :d[elete]         行を削除
:debug          :deb[ug]          コマンドをデバッグモードで実行する
:debuggreedy    :debugg[reedy]    デバッグモードのコマンドを標準入力から読み込む
:def            :def              Vim9 ユーザー関数の定義
:defcompile     :defc[ompile]     カレントスクリプト内の Vim9 ユーザー関数をコンパイルする
:delcommand     :delc[ommand]     ユーザー定義コマンドの削除
:delfunction    :delf[unction]    ユーザー定義関数の削除
:delmarks       :delm[arks]       マークを削除する
:diffupdate     :dif[fupdate]     'diff' バッファを更新する
:diffget        :diffg[et]        カレントバッファの差異を他方に合わせる
:diffoff        :diffo[ff]        差分モードをオフにする
:diffpatch      :diffp[atch]      パッチを適用した新しい差分バッファを作成する
:diffput        :diffpu[t]        他方の差異をカレントバッファに合わせる
:diffsplit      :diffs[plit]      ファイルを開きその違いを表示する
:diffthis       :diffthis         カレントウィンドウを差分ウィンドウにする
:digraphs       :dig[raphs]       ダイグラフの入力または表示
:display        :di[splay]        レジスタの内容を表示
:disassemble    :disa[ssemble]    Vim9 ユーザー関数の逆アセンブル
:djump          :dj[ump]          #define へジャンプ
:dl             :dl               'l' フラグ付き :delete の短縮形
:dlist          :dli[st]          #define をリスト表示
:doautocmd      :do[autocmd]      カレントバッファに対し自動コマンドを適用する
:doautoall      :doautoa[ll]      ロードされているバッファすべてに自動コマンドを適用する
:dp             :d[elete]p        'p' フラグ付き :delete の短縮形
:drop           :dr[op]           指定したファイルが表示されているウィンドウにジャンプするか,
                                  カレントウィンドウで開く
:dsearch        :ds[earch]        マクロ定義(#define)を表示する
:dsplit         :dsp[lit]         ウィンドウを分割し #define へジャンプ
:edit           :e[dit]           ファイルの編集
:earlier        :ea[rlier]        バッファを時間的に前の状態に戻す。アンドゥ
:echo           :ec[ho]           式の結果を表示する
:echoerr        :echoe[rr]        :echoと同じだが、エラー表示し、履歴に残す
:echohl         :echoh[l]         echoコマンドで使用する強調表示を設定する
:echomsg        :echom[sg]        :echoと同じだが、履歴に残す
:echon          :echon            :echo と同じ、ただし <EOL> を出力しない
:else           :el[se]           :if コマンドと一緒に使用する
:elseif         :elsei[f]         :if コマンドと一緒に使用する
:emenu          :em[enu]          名前を指定してメニューを実行
:enddef         :enddef           :def で開始したユーザー定義関数の終了
:endif          :en[dif]          直前の :if の終了
:endfor         :endfo[r]         直前の :for の終了
:endfunction    :endf[unction]    :function で開始したユーザー定義関数の終了
:endtry         :endt[ry]         直前の:tryを終了する
:endwhile       :endw[hile]       直前の :while の終了
:enew           :ene[w]           新しい名無しバッファを開く
:ex             :ex               ":edit" と同じ。
:execute        :exe[cute]        式の結果を実行する
:exit           :exi[t]           ":xit" と同じ。
:exusage        :exu[sage]        Exコマンドの概観
:file           :f[ile]           カレントファイルの名前を設定または表示
:files          :files            バッファリストの全ファイルを一覧表示
:filetype       :filet[ype]       ファイルタイプ検出の on/off 切換
:filter         :filt[er]         コマンドの出力をフィルターする
:find           :fin[d]           'path' の中からファイルを検索し、開く
:final          :final            Vim9 での不変変数を宣言する
:finally        :fina[lly]        :try コマンドの一部
:finish         :fini[sh]         Vim script の読み込みを終了する
:first          :fir[st]          引数リストの最初のファイルを開く
:fixdel         :fix[del]         <Del> のキーコードを設定
:fold           :fo[ld]           折畳を作成する
:foldclose      :foldc[lose]      折畳を閉じる
:folddoopen     :foldd[oopen]     閉じている折畳以外の行にコマンドを実行する
:folddoclosed   :folddoc[losed]   閉じている折畳の中の行にコマンドを実行する
:foldopen       :foldo[pen]       折畳を開く
:for            :for              for ループ
:function       :fu[nction]       ユーザー定義関数を定義
:global         :g[lobal]         パターンにマッチした行でコマンドを実行する
:goto           :go[to]           バッファ内の指定したバイト数の場所へジャンプ
:grep           :gr[ep]           'grepprg' を実行し、最初にマッチした位置へジャンプ
:grepadd        :grepa[dd]        :grepと同じだが、結果を現在のリストへ加える
:gui            :gu[i]            GUI をスタートする
:gvim           :gv[im]           GUI をスタートする
:hardcopy       :ha[rdcopy]       テキストをプリンタに出力する
:help           :h[elp]           ヘルプウィンドウを表示
:helpclose      :helpc[lose]      ヘルプウィンドウを1つ閉じる
:helpfind       :helpf[ind]       ヘルプのキーワードを入力するためのダイアログをポップアップする
:helpgrep       :helpg[rep]       ヘルプファイル検索用の ":grep"
:helptags       :helpt[ags]       指定したディレクトリのヘルプタグを作成する
:highlight      :hi[ghlight]      強調表示を定義する
:hide           :hid[e]           コマンドを実行し、必要ならカレントバッファを隠れ(hidden)バッファにする
:history        :his[tory]        コマンドラインの履歴を表示
:insert         :i[nsert]         テキストを挿入
:iabbrev        :ia[bbrev]        挿入モードを対象とする ":abbrev" コマンド
:iabclear       :iabc[lear]       挿入モードを対象とする ":abclear" コマンド
:if             :if               条件が成立した場合にコマンド群を実行
:ijump          :ij[ump]          識別子の定義へジャンプ
:ilist          :il[ist]          識別子に一致したすべての行をリスト表示
:imap           :im[ap]           挿入モードを対象とした ":map" コマンド
:imapclear      :imapc[lear]      挿入モードを対象とした ":mapclear" コマンド
:imenu          :ime[nu]          挿入モードを対象にメニュー追加
:import         :imp[ort]         Vim9: 他のスクリプトからアイテムをインポートする
:inoremap       :ino[remap]       挿入モードを対象とした ":noremap" コマンド
:inoreabbrev    :inorea[bbrev]    挿入モードを対象とした ":noreabbrev" コマンド
:inoremenu      :inoreme[nu]      挿入モードを対象とした ":noremenu" コマンド
:intro          :int[ro]          起動直後のメッセージを表示
:isearch        :is[earch]        識別子と一致した最初の行を表示
:isplit         :isp[lit]         ウィンドウを分割し、識別子の定義へジャンプ
:iunmap         :iu[nmap]         挿入モードを対象とした ":unmap" コマンド
:iunabbrev      :iuna[bbrev]      挿入モードを対象とした ":unabbrev" コマンド
:iunmenu        :iunme[nu]        挿入モードを対象にメニュー削除
:join           :j[oin]           行の結合
:jumps          :ju[mps]          ジャンプリストの表示
:k              :k                マークを設定
:keepalt        :keepa[lt]        代替ファイルを変更せずにコマンドを実行する
:keepmarks      :kee[pmarks]      マークを変更せずにコマンドを実行する
:keepjumps      :keepj[umps]      マークやジャンプリストを変更せずにコマンドを実行する
:keeppatterns   :keepp[atterns]   検索パターン履歴を変更せずにコマンドを実行する
:lNext          :lN[ext]          locationリストの前の項目の位置へ移動
:lNfile         :lNf[ile]         前のファイルの最後の項目の位置へ移動
:list           :l[ist]           行を表示
:labove         :lab[ove]         現在の行の上のlocationにジャンプ
:laddexpr       :lad[dexpr]       exprからlocationリストの項目を追加
:laddbuffer     :laddb[uffer]     バッファからlocationリストの項目を追加
:laddfile       :laddf[ile]       現在のlocationリストに項目を追加
:lafter         :laf[ter]         現在のカーソルの後ろのlocationにジャンプ
:last           :la[st]           引数リストの最後のファイルを編集
:language       :lan[guage]       言語(ロケール)を設定する
:later          :lat[er]          バッファを時間的に新しい状態に戻す。リドゥ
:lbefore        :lbef[ore]        現在のカーソルの前のlocationにジャンプ
:lbelow         :lbel[ow]         現在の行の下のlocationにジャンプ
:lbottom        :lbo[ttom]        locationウィンドウの最下へスクロールする
:lbuffer        :lb[uffer]        バッファからlocationリストを解釈し、最初のエラーへジャンプ
:lcd            :lc[d]            ウィンドウのカレントディレクトリを変更する
:lchdir         :lch[dir]         ウィンドウのカレントディレクトリを変更する
:lclose         :lcl[ose]         locationウィンドウを閉じる
:lcscope        :lcs[cope]        ":cscope" と同様だがlocationリストを使う
:ldo            :ld[o]            locationリストの各項目に対してコマンドを実行する
:lfdo           :lfd[o]           locationリストの各ファイルに対してコマンドを実行する
:left           :le[ft]           行を左寄せに整形
:leftabove      :lefta[bove]      ウィンドウが左もしくは上に分割されるようにする
:let            :let              変数またはオプションに値を設定する
:lexpr          :lex[pr]          式からlocationリストを読み込み、最初のエラーへジャンプする
:lfile          :lf[ile]          ファイルからlocationリストを読み込み、最初のエラーへジャンプする
:lfirst         :lfir[st]         指定されたlocationへジャンプする
                                  デフォルトは 最初のlocation
:lgetbuffer     :lgetb[uffer]     バッファからlocationリストを取得する
:lgetexpr       :lgete[xpr]       式からlocationリストを取得する
:lgetfile       :lg[etfile]       ファイルからlocationリストを取得する
:lgrep          :lgr[ep]          'grepprg' を実行し、最初のマッチへジャンプする
:lgrepadd       :lgrepa[dd]       :grepと同様だが現在のリストに追加する
:lhelpgrep      :lh[elpgrep]      ":helpgrep" と同様だがlocationリストを使う
:lhistory       :lhi[story]       locationリストの一覧を表示する
:ll             :ll               特定のlocationへ移動する
:llast          :lla[st]          特定のlocationへ移動する
                                  デフォルトは最後の location
:llist          :lli[st]          全てのlocationをリストする
:lmake          :lmak[e]          外部プログラム'makeprg'を実行、エラーメッセージを解釈する
:lmap           :lm[ap]           ":map!" と同じだが、Lang-Argモードも対象
:lmapclear      :lmapc[lear]      ":mapclear!" と同じだが、Lang-Argモードも対象
:lnext          :lne[xt]          次のlocationへ移動
:lnewer         :lnew[er]         新しいlocationリストへ移動
:lnfile         :lnf[ile]         次のファイルの最初のlocationへ移動
:lnoremap       :ln[oremap]       ":noremap!" と同じだが、Lang-Argモードも対象
:loadkeymap     :loadk[eymap]     次の行からEOFまでキーマップを読み込む
:loadview       :lo[adview]       カレントウィンドウにビューを読み込む
:lockmarks      :loc[kmarks]      マークを調整せずにコマンドを実行する
:lockvar        :lockv[ar]        変数をロックする
:lolder         :lol[der]         以前のlocationリストへ移動
:lopen          :lope[n]          locationウィンドウを開く
:lprevious      :lp[revious]      前のlocationへ移動
:lpfile         :lpf[ile]         前のファイルの最後のlocationへ移動
:lrewind        :lr[ewind]        指定されたlocationへ移動
                                  デフォルトは最初のlocation
:ls             :ls               すべてのバッファを表示
:ltag           :lt[ag]           タグへジャンプし、マッチしたタグをlocationリストに追加する
:lunmap         :lu[nmap]         ":unmap!" と同じだが、Lang-Argモードも対象
:lua            :lua              Lua コマンドを実行
:luado          :luad[o]          各行に対して Lua コマンドを実行
:luafile        :luaf[ile]        Lua スクリプトファイルを実行
:lvimgrep       :lv[imgrep]       ファイルからパターンを検索する
:lvimgrepadd    :lvimgrepa[dd]    :vimgrepと同様だが、locationリストに追加する
:lwindow        :lw[indow]        locationウィンドウを開閉する
:move           :m[ove]           行を移動する
:mark           :ma[rk]           マークを設定
:make           :mak[e]           外部プログラム 'makeprg' を実行し、エラーメッセージを解釈する
:map            :map              マップの設定または表示
:mapclear       :mapc[lear]       ノーマルモードとビジュアルモードを対象にマップをクリア
:marks          :marks            すべてのマークを表示
:match          :mat[ch]          指定したパターンの文字を強調表示する
:menu           :me[nu]           新しいメニュー項目を追加
:menutranslate  :menut[ranslate]  翻訳したメニュー項目を追加する
:messages       :mes[sages]       直前に表示されたメッセージの表示
:mkexrc         :mk[exrc]         現在のマップと設定をファイルに書き出す
:mksession      :mks[ession]      セッション情報をファイルに書き出す
:mkspell        :mksp[ell]        スペルファイル .splを生成する
:mkvimrc        :mkv[imrc]        現在のマップと設定をファイルに書き出す
:mkview         :mkvie[w]         カレントウィンドウのビューをファイルに保存する
:mode           :mod[e]           スクリーンモードを表示または変更する
:mzscheme       :mz[scheme]       MzSchemeコマンドを実行する
:mzfile         :mzf[ile]         MzSchemeスクリプトファイルを実行する
:nbclose        :nbc[lose]        現在の Netbeans セッションを閉じる
:nbstart        :nbs[art]         新しい Netbeans セッションを開始する
:nbkey          :nb[key]          キーをNetbeansに渡す
:next           :n[ext]           引数リストの次のファイルを開く
:new            :new              新規に空のウィンドウを作成する
:nmap           :nm[ap]           ノーマルモードを対象とする ":map" コマンド
:nmapclear      :nmapc[lear]      ノーマルモードのすべてのマップを削除する
:nmenu          :nme[nu]          ノーマルモードのメニューを追加する
:nnoremap       :nn[oremap]       ノーマルモードを対象とする ":noremap" コマンド
:nnoremenu      :nnoreme[nu]      ノーマルモードを対象とする ":noremenu" コマンド
:noautocmd      :noa[utocmd]      自動コマンドを実行せずにコマンドを実行する
:noremap        :no[remap]        再マップされないマップを定義する
:nohlsearch     :noh[lsearch]     一時的に 'hlsearch' の強調表示をやめる
:noreabbrev     :norea[bbrev]     再マップされない短縮入力を定義する
:noremenu       :noreme[nu]       再マップされないメニューを定義する
:normal         :norm[al]         ノーマルモードのコマンドを実行する
:noswapfile     :nos[wapfile]     スワップファイルを作らずにコマンドを実行する
:number         :nu[mber]         行番号を表示
:nunmap         :nun[map]         ノーマルモードを対象とする ":unmap" コマンド
:nunmenu        :nunme[nu]        ノーマルモードのメニューを削除
:oldfiles       :ol[dfiles]       viminfo ファイルに記録されたマークを持つファイルを表示する
:open           :o[pen]           openモードを開始(未実装)
:omap           :om[ap]           Operator-pending モードを対象とする ":map" コマンド
:omapclear      :omapc[lear]      Operator-pending モードのマップをすべて削除
:omenu          :ome[nu]          Operator-pending モードのメニューを追加
:only           :on[ly]           カレントウィンドウ以外のウィンドウをすべて閉じる
:onoremap       :ono[remap]       Operator-pending モードを対象とする ":noremap" コマンド
:onoremenu      :onoreme[nu]      Operator-pending モードを対象とする ":noremenu" コマンド
:options        :opt[ions]        オプションウィンドウを開く
:ounmap         :ou[nmap]         Operator-pending モードを対象とした ":unmap" コマンド
:ounmenu        :ounme[nu]        Operator-pending モードのメニューを削除
:ownsyntax      :ow[nsyntax]      ウィンドウのローカル構文強調を新たに設定する
:packadd        :pa[ckadd]        'packpath' からプラグインを追加する
:packloadall    :packl[oadall]    'packpath' 下の全プラグインをロードする
:pclose         :pc[lose]         プレビューウィンドウを閉じる
:pedit          :ped[it]          プレビューウィンドウでファイルを開く
:perl           :pe[rl]           Perl コマンドを実行
:print          :p[rint]          行単位で印刷する
:profdel        :profd[el]        関数やスクリプトのプロファイリングを停止する
:profile        :prof[ile]        関数やスクリプトのプロファイリングをする
:promptfind     :pro[mptfind]     GUIの検索ダイアログを開く
:promptrepl     :promptr[epl]     GUIの検索・置換ダイアログを開く
:perldo         :perld[o]         1行ずつ Perl コマンドを実行
:pop            :po[p]            タグスタックの1つ古いエントリへジャンプ
:popup          :popup            指定した名前のメニューをポップアップ表示する
:ppop           :pp[op]           プレビューウィンドウで ":pop" を実行
:preserve       :pre[serve]       すべてのテキストをスワップファイルに書き出す
:previous       :prev[ious]       引数リスト中の前のファイルを読み込む
:psearch        :ps[earch]        ":ijump"と同じだが、結果をプレビューウィンドウで表示する
:ptag           :pt[ag]           プレビューウィンドウでタグを表示
:ptNext         :ptN[ext]         プレビューウィンドウで :tNext を実行
:ptfirst        :ptf[irst]        プレビューウィンドウで:trewind を実行
:ptjump         :ptj[ump]         プレビューウィンドウで :tjump を実行、タグを表示
:ptlast         :ptl[ast]         プレビューウィンドウで :tlast を実行
:ptnext         :ptn[ext]         プレビューウィンドウで :tnext を実行
:ptprevious     :ptp[revious]     プレビューウィンドウで :tprevious を実行
:ptrewind       :ptr[ewind]       プレビューウィンドウで :trewind を実行
:ptselect       :pts[elect]       プレビューウィンドウで :tselect を実行、タグを表示
:put            :pu[t]            テキストにレジスタの内容を挿入
:pwd            :pw[d]            カレントディレクトリを表示
:py3            :py3              Python 3 コマンドを実行
:python3        :python3          :py3 と同じ
:py3do          :py3d[o]          各行に対して Python 3 コマンドを実行
:py3file        :py3f[ile]        Python 3 スクリプトファイルを実行
:python         :py[thon]         Python コマンドを実行
:pydo           :pyd[o]           各行に対して Python コマンドを実行
:pyfile         :pyf[ile]         Python スクリプトファイルを実行
:pyx            :pyx              python_x コマンドを実行
:pythonx        :pythonx          :pyx と同じ
:pyxdo          :pyxd[o]          各行に対して python_x コマンドを実行
:pyxfile        :pyxf[ile]        python_x スクリプトファイルを実行
:quit           :q[uit]           カレントウィンドウを閉じる(ウィンドウが1つなら Vim を終了)
:quitall        :quita[ll]        Vim を終了
:qall           :qa[ll]           Vim を終了
:read           :r[ead]           テキストにファイルを挿入
:recover        :rec[over]        スワップファイルからファイルを復元
:redo           :red[o]           1回のアンドゥをリドゥする
:redir          :redi[r]          ファイルまたはレジスタにメッセージをリダイレクトする
:redraw         :redr[aw]         画面を再描画する
:redrawstatus   :redraws[tatus]   ステータスラインを再描画する
:redrawtabline  :redrawt[abline]  タブページ行を再描画する
:registers      :reg[isters]      レジスタの内容を表示
:resize         :res[ize]         カレントウィンドウの高さを変更
:retab          :ret[ab]          タブの大きさを変更
:return         :retu[rn]         ユーザー関数から戻る
:rewind         :rew[ind]         引数リストの先頭のファイルを開く
:right          :ri[ght]          テキストを右寄せに整形
:rightbelow     :rightb[elow]     ウィンドウが右もしくは下に分割されるようにする
:ruby           :rub[y]           Rubyのコマンドを実行する
:rubydo         :rubyd[o]         各行に対してRubyのコマンドを実行する
:rubyfile       :rubyf[ile]       Rubyスクリプトファイルを実行する
:rundo          :rund[o]          アンドゥ情報をファイルから読み込む
:runtime        :ru[ntime]        Vim script を'runtimepath'から探して実行する
:rviminfo       :rv[iminfo]       viminfo ファイルを読み込む
:substitute     :s[ubstitute]     テキストの置換
:sNext          :sN[ext]          ウィンドウを分割して、引数リストの前のファイルを開く
:sandbox        :san[dbox]        サンドボックスでコマンドを実行する
:sargument      :sa[rgument]      ウィンドウを分割して、引数リストの指定ファイルを開く
:sall           :sal[l]           引数リストのすべてのファイルをウィンドウを作成して開く
:saveas         :sav[eas]         別の名前でファイルを保存する
:sbuffer        :sb[uffer]        ウィンドウを分割してバッファリストの指定したバッファを開く
:sbNext         :sbN[ext]         ウィンドウを分割してバッファリストの前のバッファを開く
:sball          :sba[ll]          バッファリストのすべてのバッファをウィンドウを作成して開く
:sbfirst        :sbf[irst]        ウィンドウを分割してバッファリストの最初のバッファを開く
:sblast         :sbl[ast]         ウィンドウを分割してバッファリストの最後のバッファを開く
:sbmodified     :sbm[odified]     ウィンドウを分割してバッファリストの変更済みバッファを開く
:sbnext         :sbn[ext]         ウィンドウを分割してバッファリストの次のバッファを開く
:sbprevious     :sbp[revious]     ウィンドウを分割してバッファリストの前のバッファを開く
:sbrewind       :sbr[ewind]       ウィンドウを分割してバッファリストの最初のバッファを開く
:scriptnames    :scr[iptnames]    実行済みVim script の名前を一覧表示する
:scriptencoding :scripte[ncoding] Vim script が使用しているエンコーディングを指定する
:scriptversion  :scriptv[ersion]  使用している Vim script のバージョンを指定する
:scscope        :scs[cope]        ウィンドウを分割してcscopeコマンドを実行する
:set            :se[t]            オプションを表示または設定する
:setfiletype    :setf[iletype]    まだ設定されていなければ 'filetype' を設定する
:setglobal      :setg[lobal]      グローバルオプションを表示もしくは設定する
:setlocal       :setl[ocal]       ローカルオプションを表示もしくは設定する
:sfind          :sf[ind]          ウィンドウを分割して、'path' にあるファイルを開く
:sfirst         :sfir[st]         ウィンドウを分割して引数リストの最初のファイルを開く
:shell          :sh[ell]          シェルを実行する
:simalt         :si[malt]         Win32 GUI: Windows ALT キーをシミュレートする
:sign           :sig[n]           目印を取り扱うコマンド
:silent         :sil[ent]         実行したコマンドの出力を抑制する
:sleep          :sl[eep]          数秒間何もしない
:slast          :sla[st]          ウィンドウを分割して引数リストの最後のファイルを開く
:smagic         :sm[agic]         'magic' オプションの下で :substitute を実行
:smap           :smap             ":map" と同様。選択モード用
:smapclear      :smapc[lear]      選択モードのすべてのマップを削除する
:smenu          :sme[nu]          選択モードのメニューを追加する
:smile          :smi[le]          ユーザーを幸せにする
:snext          :sn[ext]          ウィンドウを分割して引数リストの次のファイルを開く
:snomagic       :sno[magic]       'nomagic' オプションの下で :substitute を実行
:snoremap       :snor[emap]       ":noremap" と同様。選択モード用
:snoremenu      :snoreme[nu]      ":noremenu" と同様。選択モード用
:sort           :sor[t]           行をソートする
:source         :so[urce]         Vim or Ex コマンドをファイルから読み込む
:spelldump      :spelld[ump]      ウィンドウを分割し、正しい単語を列挙する
:spellgood      :spe[llgood]      スペルチェック用に正しい単語を登録する
:spellinfo      :spelli[nfo]      読み込んでいるスペルファイルの情報を表示する
:spellrare      :spellra[re]      スペルチェック用にレアな単語を追加する
:spellrepall    :spellr[epall]    最後のz=と同様にすべての間違った単語を置換
:spellundo      :spellu[ndo]      正しいまたは間違った単語を削除
:spellwrong     :spellw[rong]     スペリングの間違いを登録する
:split          :sp[lit]          カレントウィンドウを分割
:sprevious      :spr[evious]      ウィンドウを分割して引数リストの前のファイルを開く
:srewind        :sre[wind]        ウィンドウを分割して引数リストの最初のファイルを開く
:stop           :st[op]           Vimをサスペンドする
:stag           :sta[g]           ウィンドウを分割して、タグへジャンプする
:startinsert    :star[tinsert]    挿入モードを開始する
:startgreplace  :startg[replace]  仮想置換モードを開始する
:startreplace   :startr[eplace]   置換モードを開始する
:stopinsert     :stopi[nsert]     挿入モードを終了する
:stjump         :stj[ump]         ウィンドウを分割して、":tjump" を実行
:stselect       :sts[elect]       ウィンドウを分割して、":tselect" を実行
:sunhide        :sun[hide]        ":unhide" と同じ。
:sunmap         :sunm[ap]         ":unmap" と同様。選択モード用
:sunmenu        :sunme[nu]        選択モードのメニューを削除する
:suspend        :sus[pend]        ":stop" と同じ。
:sview          :sv[iew]          ウィンドウを分割してファイルを読み込み専用で開く
:swapname       :sw[apname]       現在のスワップファイルの名前を表示
:syntax         :sy[ntax]         構文強調表示 (syntax highlighting)
:syntime        :synti[me]        構文強調表示の速度を測定する
:syncbind       :sync[bind]       ウィンドウのスクロール状態を同期する
:t              :t                ":copy" と同じ。
:tNext          :tN[ext]          後方へ検索し一致したタグ位置へジャンプ
:tabNext        :tabN[ext]        前のタブページへ移動
:tabclose       :tabc[lose]       現在のタブページを閉じる
:tabdo          :tabdo            各タブページでコマンドを実行する
:tabedit        :tabe[dit]        新しいタブページでファイルを開く
:tabfind        :tabf[ind]        'path'からファイルを探し新しいタブページで開く
:tabfirst       :tabfir[st]       最初のタブページへ移動
:tablast        :tabl[ast]        最後のタブページへ移動
:tabmove        :tabm[ove]        タブページの位置を移動
:tabnew         :tabnew           新しいタブページでファイルを編集する
:tabnext        :tabn[ext]        次のタブページへ移動
:tabonly        :tabo[nly]        現在のタブページ以外をすべて閉じる
:tabprevious    :tabp[revious]    前のタブページへ移動
:tabrewind      :tabr[ewind]      最初のタブページへ移動
:tabs           :tabs             タブページとその中身を列挙
:tab            :tab              新しいウィンドウを開くとき新しいタブを作る
:tag            :ta[g]            タグを検索しジャンプする
:tags           :tags             タグスタックの内容を表示
:tcd            :tcd              タブページのカレントディレクトリを変更する
:tchdir         :tch[dir]         タブページのカレントディレクトリを変更する
:tcl            :tc[l]            Tcl コマンドを実行
:tcldo          :tcld[o]          各行の Tcl コマンドを実行
:tclfile        :tclf[ile]        Tcl スクリプトファイルを実行
:tearoff        :te[aroff]        メニューを切り離す
:terminal       :ter[minal]       端末ウィンドウを開く
:tfirst         :tf[irst]         複数一致した内の最初のタグへジャンプ
:throw          :th[row]          例外を投げる
:tjump          :tj[ump]          ":tselect" と同様、ただし一致したタグが1つしかない場合、その場所へジャンプ
:tlast          :tl[ast]          直前に一致したタグ位置へジャンプ
:tlmenu         :tlm[enu]         端末ジョブモードのメニューを追加する
:tlnoremenu     :tln[oremenu]     ":noremenu" と同様だが端末ジョブモード用
:tlunmenu       :tlu[nmenu]       端末ジョブモードのメニューを削除する
:tmapclear      :tmapc[lear]      端末ジョブモードのすべてのマップを削除する
:tmap           :tma[p]           ":map" と同様。端末ジョブモード用
:tmenu          :tm[enu]          ツールチップメニューを定義する
:tnext          :tn[ext]          タグを前方検索し、ジャンプ
:tnoremap       :tno[remap]       ":noremap" と同様。端末ジョブモード用
:topleft        :to[pleft]        ウィンドウが最も左もしくは最も上に分割されるようにする
:tprevious      :tp[revious]      タグを後方検索し、ジャンプ
:trewind        :tr[ewind]        最初に一致したタグ位置へジャンプ
:try            :try              コマンドを実行し発生したエラーや例外を処理する
:tselect        :ts[elect]        一致したタグを一覧表示し、ジャンプ先のタグを選択
:tunmap         :tunma[p]         ":unmap" と同様。端末ジョブモード用
:tunmenu        :tu[nmenu]        ツールチップメニューを削除
:undo           :u[ndo]           最後の変更を取り消す
:undojoin       :undoj[oin]       次の変更を前のアンドゥブロックと連結する
:undolist       :undol[ist]       アンドゥツリーのリーフを列挙する
:unabbreviate   :una[bbreviate]   短縮入力を削除
:unhide         :unh[ide]         バッファリストのメモリに
                                  ロードされているすべてのバッファをウィンドウを作成して開く
:unlet          :unl[et]          変数を削除
:unlockvar      :unlo[ckvar]      変数をアンロックする
:unmap          :unm[ap]          マップを削除
:unmenu         :unme[nu]         メニューを削除
:unsilent       :uns[ilent]       コマンドを silent でなく実行する
:update         :up[date]         バッファ内容が変更されていれば、ファイルに書き出す
:vglobal        :v[global]        パターンにマッチしない行でコマンドを実行する
:var            :var              Vim9 での変数を宣言する
:version        :ve[rsion]        バージョン番号その他の情報を表示
:verbose        :verb[ose]        'verbose' を一時設定してコマンドを実行する
:vertical       :vert[ical]       ウィンドウが垂直分割されるようにする
:vim9script     :vim9[script]     Vim9 スクリプトファイルであることを示す
:vimgrep        :vim[grep]        複数ファイルからパターンを検索する
:vimgrepadd     :vimgrepa[dd]     :vimgrepと同様だが現在のリストに追加
:visual         :vi[sual]         ":edit" と同じ、ただし "Ex" モードから抜ける。
:viusage        :viu[sage]        ノーマルモードコマンドの概観
:view           :vie[w]           読み込み専用でファイルを開く
:vmap           :vm[ap]           ビジュアル・選択モードを対象とする ":map" コマンド
:vmapclear      :vmapc[lear]      ビジュアル・選択モードのマッピングをすべて削除
:vmenu          :vme[nu]          ビジュアル・選択モードのメニューを追加
:vnew           :vne[w]           新しいウィンドウを垂直分割して作る
:vnoremap       :vn[oremap]       ビジュアル・選択モードを対象とする ":noremap" コマンド
:vnoremenu      :vnoreme[nu]      ビジュアル・選択モードを対象とする ":noremenu" コマンド
:vsplit         :vs[plit]         カレントウィンドウを垂直分割する
:vunmap         :vu[nmap]         ビジュアル・選択モードを対象とする ":unmap" コマンド
:vunmenu        :vunme[nu]        ビジュアルモードのメニューを削除
:windo          :windo            各ウィンドウに対してコマンドを実行する
:write          :w[rite]          ファイルに保存
:wNext          :wN[ext]          ファイルに保存して、引数リストの直前のファイルを開く
:wall           :wa[ll]           (変更した) すべてのバッファを保存
:while          :wh[ile]          与えた条件を満たしている限りループする
:winsize        :wi[nsize]        ウィンドウサイズを取得もしくはセットする (古いコマンド)
:wincmd         :winc[md]         ウィンドウコマンド(CTRL-W)を実行する
:winpos         :winp[os]         ウィンドウの位置を取得もしくはセットする
:wnext          :wn[ext]          ファイルに保存して、引数リストの次のファイルを開く
:wprevious      :wp[revious]      ファイルに保存して、引数リストの直前のファイルを開く
:wq             :wq               ファイルに保存して、ウィンドウもしくは Vim を終了
:wqall          :wqa[ll]          すべての変更済みバッファを保存し、Vim を終了
:wundo          :wu[ndo]          アンドゥ情報をファイルに保存する
:wviminfo       :wv[iminfo]       viminfo ファイルに保存
:xit            :x[it]            バッファが変更されていたら保存し、ウィンドウを 閉じる
:xall           :xa[ll]           ":wqall" と同じ。
:xmapclear      :xmapc[lear]      ビジュアルモード時のマッピングを全て削除する
:xmap           :xm[ap]           ":map" と同様。ビジュアルモード用
:xmenu          :xme[nu]          ビジュアルモード時にメニューを追加する
:xrestore       :xr[estore]       Xサーバーの接続を復元する
:xnoremap       :xn[oremap]       ":noremap" と同様。ビジュアルモード用
:xnoremenu      :xnoreme[nu]      ":noremenu" と同様。ビジュアルモード用
:xunmap         :xu[nmap]         ":unmap" と同様。ビジュアルモード用
:xunmenu        :xunme[nu]        ビジュアルモード時にメニューを削除する
:yank           :y[ank]           行をレジスタへヤンク
:z              :z                行を表示
:~              :~                直前に実行した ":substitute" を実行
```



