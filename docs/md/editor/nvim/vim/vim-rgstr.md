
# register


## register を確認する

```
:registers
```

or

```
:reg
```


## register a に登録する

```
"ayy
```


## cmd mode で paste

```
c-r <rgstr-num>
```

- 0 - 9
- 直近の register num は 0


## rgstr list

```
no         rgstr name    desc
01                       無名 register
02 - 11    0 - 9         番号付き register
12         -             小削除用 register
13 - 38    a - z         名前付き register
39 - 64    A - Z
65         :             cmdline ltst
66         .             ins str
67         %             file name
68         #             代替 file ?
69         =             expression register
70         *             clip board
71         +             clip board
72         ~             drug and drop
73         _             消去専用 register
74         /             最終検索パターン用 register
```


## ref

- https://vim.blue/vim-all-register/


