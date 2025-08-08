
# uconv

- iconv よりもいまは uconv を推奨 ということだったと思ったが,  
  その理由は 忘れた..
- ref
  - https://qiita.com/ko1nksm/items/7c31a2759579e6a1b65b


## install

```
brew install icu4c
```

path

```fish
alias uconv '/home/linuxbrew/.linuxbrew/Cellar/icu4c@77/77.1/bin/uconv
```


## cnv

```
cat memo-utf8.md | uconv -f UTF-8     -t SHIFT_JIS > memo-sjis.md
```

```
cat memo-sjis.md | uconv -f SHIFT_JIS -t UTF-8     > memo-utf8.md
```


## code list

```
wip:
```


