
# git diff


## 基本

### 同種のものを引数で指定する場合

`old` `new` の順

```
git diff old new
```


## 概要のみ表示 ( file の中身を表示しない )

### 差分情報のみを表示

```
git diff --stat
```


### file_name のみ表示

```
git diff --name-only
```


## 各種 diff 表示

### work tree と staged の diff

```
git diff
```


### work tree と HEAD ( repo latest ) の diff

```
git diff HEAD
```


### staged と HEAD ( repo latest ) の diff

```
git diff --staged
```


### staged と commit latest の diff

```
git diff --cached
```

wip: 1つ上のと違いは.. ?? ( 同じでは ? )


### branch1 と branch2 の diff

```
git diff branch1 branch2
```

`clone` 直後などの場合, `git switch` するなどしたあとでないと,
できない ( ときがあった )


### commit prv と commit latest の diff

```
git diff HEAD~..HEAD
```


### commit1 と commit2 の diff

```
git diff SHA1..SHA2
```


### branch local と branch remote の diff

```
git diff main origin/main
```

^ fetch しないとうまくいかない ?

file を指定する場合は ?



## diff 結果を vimdiff で見る

```
git difftool file_path
```



