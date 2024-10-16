
# date


## date format y m d h s を 個別に覚えるより `%F %T` がおすすめ

ex

```
$ date +"%F %T"
2024-07-05 13:21:30
```


## date format から unix time

```
date --date="2024-07-02T11:00:00" +"%s"
```


## date sub  -  経過時間の算出  -  引き算, 減算

unix time にして 引き算

```
set time_e "2024-07-02T11:17:08"
set time_s "2024-07-02T10:56:57"

math -s1                          \
 \(                               \
   ( date --date=$time_e +"%s" )  \
 - ( date --date=$time_s +"%s" )  \
 \) / 60                          \
```



