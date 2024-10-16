
# awscli dynamo db


## table lst

```
aws dynamodb list-tables
```


## table describe

```
aws dynamodb describe-table --table-name tbl_name
{
    "Table": {
        "AttributeDefinitions": [
            {
                "AttributeName": "created_at",
                "AttributeType": "S"
            },
            {
                "AttributeName": "post_id",
                "AttributeType": "N"
        ( 省略 )
```


## 予約語

https://dev.classmethod.jp/articles/dynamodb_handling_reserved_keyword/



## ref

https://www.wakuwakubank.com/posts/675-aws-cli-dynamodb/

https://qiita.com/ekzemplaro/items/93c0aef433a2b633ab4a

https://docs.aws.amazon.com/ja_jp/cli/latest/userguide/cli-services-dynamodb.html

iam setting

https://www.hands-lab.com/tech/t4379/



