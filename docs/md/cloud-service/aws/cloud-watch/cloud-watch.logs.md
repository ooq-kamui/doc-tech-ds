
# cloud watch  -  logs


## log group list

```
aws logs describe-log-groups
```


## tail

```
aws logs tail             \
  --follow [log_grp_name] \
```

### 直近 30m の log から  -  tail

```
--since 30m
```

単位

```
s : second : 秒
m : minute : 分
h : hour   : 時間
d : day    : 日
w : week   : 週
```

### filter  -  tail

```
aws logs tail             \
  --follow [log_grp_name] \
  --filter-pattern [ptn]  \
```

ex

```
aws logs tail                        \
  --follow "/aws/lambda/fnc01-dev"   \
  --filter-pattern "string1 string2" \
```


## filter ( search )

```
aws logs filter-log-events        \
  --log-group-name [log_grp_name] \
  [opt]                           \
```

opt

```
--filter-pattern : ログの絞り込み条件を指定
--start-time     : 表示するログの開始時間をエポックで指定
--end-time       : 表示するログの終了時間をエポックで指定

--query          : aws cli 側 で結果のフィルタリングや関数適用を行う
--output         : 出力形式の指定
```

ex

```
$ aws logs filter-log-events                                     \
  --log-group-name "/aws/lambda/fnc01-dev"                       \
  --filter-pattern "string1 string2"                             \
  --start-time $( date --date='2024-07-01 00:00:00.000' +%s%3N ) \
```

```
aws logs filter-log-events                                  \
  --log-group-name [log_grp01]                              \
  --filter-pattern [string1 string2]                        \
  --start-time     [unix time]                              \
  --end-time       [unix time]                              \
  --query 'sort_by(events, &timestamp)[].{message:message}' \
  --output text                                             \
```


## クライアント側のフィルタリングの指定

sort_byでソートしつつ, 必要な項目に絞り込む

```
--query 'sort_by(events, &timestamp)[].{message:message}'
```

```
--query 'sort_by(events, &timestamp)[].{timestamp:timestamp,message:message}'
```

絞り込まない場合の出力項目

```
logStreamName
timestamp
message
ingestionTime
eventId
```



