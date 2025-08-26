
# jq


## install

```
brew install jq
```


## 整形

単に jq を通せば ok

```
cat a.json | jq
```


## 抽出

### basic

```
.     root
[]    array
xxx   obj-key
```


### json を csv に変換

- obj の 配列 の 1階層目の key を col として, csv にする

```
cat list.json | jq -r '.[] | [.key01, .key02] | @csv'
```

ex

json の root に obj 配列 が ある場合

```
[
  {
    "name": "name01",
    "key01": "val-01-01",
    "key02": "val-01-02"
  },
  {
    "name": "name02",
    "key01": "val-02-01",
    "key02": "val-02-02"
  },
  {
    "name": "name03",
    "key01": "val-03-01",
    "key02": "val-03-02"
  }
]
```

```
cat itm.json | jq -r '.[] | [.name, .key01] | @csv'
```

obj 配列 が root でない場合

```
{
  "Items": [
    {
      "name": "name01",
      "key01": "val-01-01",
      "key02": "val-01-02"
    },
    {
      "name": "name02",
      "key01": "val-02-01",
      "key02": "val-02-02"
    },
    {
      "name": "name03",
      "key01": "val-03-01",
      "key02": "val-03-02"
    }
  ]
}
```

```
cat itm.json | jq -r '.Items[] | [.name, .key01] | @csv'
```

```
"name01","val-01-01"
"name02","val-02-01"
"name03","val-03-01"
```


### ある位置より親側の値を表形式で出力

```
wip:  できないかも ??
```


## faq

### シングルクォート or ダブルクォート ?

基本,
json の key 文字列 の 囲みは
ダブルクォート

jq も ダブルクォート しか受け付けない


