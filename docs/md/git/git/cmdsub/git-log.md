
# git log


## commit history を表示する

```
git log
```


## branch 指定

```
git log branch1
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


## file 指定

commit id のみ 表示

```
git log xxx/xxx/xxx.txt
```

diff も表示

```
git log -p xxx/xxx/xxx.txt
```


---

## 関連

- [ある commit の file list を表示する ](git.show.md )



## 最後にプッシュされた以降の変更履歴

```
git log origin/main..main
```



