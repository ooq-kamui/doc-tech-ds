
# awscli dynamo db


## del ( del )

```
aws dynamodb delete-item --table-name fe-wa.m \
--key '{ "prt": {"S": "battle"} }' \
--return-values ALL_OLD \
--return-consumed-capacity TOTAL \
--return-item-collection-metrics SIZE
```



