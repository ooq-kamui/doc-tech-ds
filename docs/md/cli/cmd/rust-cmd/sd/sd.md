
# sd

cat test.txt
abcABCabcABC

sd abc 012 test.txt 
012012012012

デフォルトでは smart case でマッチする


大文字小文字を区別 する/しない
sd -f c abc 012 test.txt
012ABC012ABC

sd -f i ABC 012 test.txt
012012012012


ファイルを上書き保存
sd -i abc 012 test.txt


正規表現
echo 'abc   ' | sd '\s+$' ''
abc

-s オプションを指定すると正規表現を無効にできる
echo 'abc((([])))' | sd -s '((([])))' ''
abc


一括置換  -  fdコマンドと組み合わせた
for file in $(fd -t f)
do
  cp "$file" "$file.bk"
  sd -i 'from "react"' 'from "preact"' "$file"
done



