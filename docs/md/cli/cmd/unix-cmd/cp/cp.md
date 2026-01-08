
# cp


## ln を ln のまま cp

```
cp -d
```

or 

```
cp -P
```


## faq

### `cp -i` と `cp -f` がバッティングのとき

基本は `cp -i` にしたいため, alias で `cp -i` にしているが,  
directory の cp は `cp -rf` にしたい場合

fish なら

```fish
command cp -rf dir01 dir02
```



