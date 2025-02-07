
# aws cli dynamo db


## get-item

```
aws dynamodb get-item  \
  --table-name fe-wa.m \
  --key '{"prt": {"S": "chara" }, "id": { "S": "camilla" } }'
```


## query

```
aws dynamodb query                                     \
  --table-name fe-wa.m                                 \
  --key-condition-expression 'prt = :prt and id = :id' \
  --expression-attribute-values '{":prt":{"S":"chara"}, ":id":{"S": "camilla"}}'
```


## scan

```
aws dynamodb scan                  \
  --table-name fe-wa.m             \
  --filter-expression 'msg = :msg' \
  --expression-attribute-values '{ ":msg": { "S": "cc" } }'
```


## select count

```
aws dynamodb query                                             \
  --table-name fe-wa.t                                         \
  --key-condition-expression 'prt = :prt '                     \
  --expression-attribute-values '{ ":prt": { "S": "chara" } }' \
  --select COUNT
```


## 条件, ~ で始まる

```
  --key-condition-expression 'begins_with(id, :id) ' \
```

## val を 別file

```
  --expression-attribute-values file://query-val.json
```


## text 形式で output

```
  --output text \
```


