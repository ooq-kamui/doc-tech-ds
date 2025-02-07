
# aws cli  -  dynamo db


## del ( del )

```
aws dynamodb delete-item                \
  --table-name fe-wa.m                  \
  --key '{ "prt": {"S": "battle"} }'    \
  --return-values ALL_OLD               \
  --return-consumed-capacity TOTAL      \
  --return-item-collection-metrics SIZE
```


## faq

- 条件に一致する複数レコード を 一度に削除する command は ない



## ref

https://docs.aws.amazon.com/ja_jp/amazondynamodb/latest/developerguide/SQLtoNoSQL.DeleteData.html


