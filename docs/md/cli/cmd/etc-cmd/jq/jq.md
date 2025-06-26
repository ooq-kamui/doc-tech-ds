
# jq


## install

```
brew install jq
```


## 使いかた

### 整形

単に jq を通せば ok

```
cat a.json | jq
```


### 抽出

#### basic

```
.     root
[]    array
xxx   obj-key
```


#### 表形式で出力

```
_ cat itm.json
{
  "items": [
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
_
_
_ cat itm.json | jq -r '.items[] | [.name, .key01] | @csv'
"name01","val-01-01"
"name02","val-02-01"
"name03","val-03-01"
```


#### ある位置より親側の値を表形式で出力

```
wip:  できないかも ??
```


## faq

### シングルクォート or ダブルクォート ?

基本,
json の key 文字列 の 囲みは
ダブルクォート

jq も ダブルクォート しか受け付けない


