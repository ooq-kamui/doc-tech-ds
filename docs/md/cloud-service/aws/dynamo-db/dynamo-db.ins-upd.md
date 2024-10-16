
# awscli dynamo db


## item put ( ins )

```
aws dynamodb put-item --table-name fe-wa.m \
--item '{"prt": { "S": "chara"   }, "id": { "S": "camilla" }, "name": { "S": "カミラ" } }'
```


## item upd ( upd )

```
aws dynamodb update-item --table-name fe-wa.m \
--key '{ "prt": {"S":"xx"}, "id": {"S": "xxx" }}' \
--update-expression 'SET chara = :chara ' \
--expression-attribute-values '{ ":chara": {"S": "kamui" } }' \
--return-values ALL_NEW
```



