
# pm2


## 確認
```
pm2 list
```


## 起動
```
pm2 start xxx


# pm2 start node-red
pm2 start /usr/local/bin/node-red -- -v
```


## 停止
```
pm2 stop xxx


# pm2 stop node-red
pm2 stop node-red
```



## log 確認
```
pm2 logs xxx


# pm2 logs node-red
pm2 logs node-red
```


## 確認  -  詳細 ( info )
```
pm2 info xxx


# pm2 info node-red
pm2 info node-red
```


## app status 確認
```
pm2 show xxx


# pm2 show node-red
pm2 show node-red
```



