
# git log


## commit history を表示する

```
git log
```


## branch 指定

```
git log branch01
```

remote tracking branch を指定すれば remote の log を見ることもできる

```
git log origin/branch01
```


## 日付の表示形式を指定

```
git log --date=format:'%Y-%m-%d %H:%M:%S'
```

```
git log --date=iso-local
```

config

```
git config --global log.date iso-local
```


## file から 指定

commit id のみ 表示

```
git log xxx/xxx/xxx.txt
```

diff も表示

```
git log -p xxx/xxx/xxx.txt
```


## 最後に push した以降 の log

```
git log origin/main..main
```


## tree 表示

```
git log --graph
```


## git log の format を変える

```
git log --pretty=format:<format-string>
```

### `format-string`

```
%ad  : date : 通常表示
%ar  : date : ago 表示

```

ex

```
git log --pretty=format:"%x09%C(auto) %h %Cgreen %ar %Creset%x09by %C(cyan ul)%an%Creset  %x09%C(auto)%s %d"
```



## 関連

### ある commit の file list

```
git show --name-only <commit-id>
```



