
# cp


## ln を ln のまま cp

```
cp -d
```

or 

```
cp -P
```


## cp 先がすでにあるときに 自動で backup

```
cp -b a.md b.md
```

or

```
cp --backup a.md b.md
```

### backup 方式 を指定

```
simple   / never | file2.txt~                                |
numbered / t     | file2.txt.~1~                             |
existing / nil   | 既に番号付きがあれば番号, なければ simple |
none     / off   | バックアップしない                        |
```

```
cp --backup=numbered a.md b.md
```

- `-b` では 方式の指定はできない

### 環境変数で 方式を 指定しておく

```fish
set -gx VERSION_CONTROL numbered
```


## faq

### `cp -i` と `cp -f` がバッティングのとき

基本は `cp -i` にしたいため, alias で `cp -i` にしているが,  
directory の cp は `cp -rf` にしたい場合

fish なら

```fish
command cp -rf dir01 dir02
```


