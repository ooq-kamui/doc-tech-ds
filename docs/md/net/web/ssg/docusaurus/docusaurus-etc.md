
# etc


## download file name に hash 値 を付けない

- download file の file name には default では 勝手に hash 値が付与される
- これを 付けないようにするには, link url の 頭 に `pathname://` を付ける
- file 設置 dir は static の配下にする

ex

`/static/sh/dl-file-name.zip` に置いたとすると

```
  [file-name](pathname:///sh/dl-file-name.zip)
```


## `memo` dir, file name

dir name, file name を `memo` にすると, 挙動が特殊なよう

詳細, 未調査

ひとまず, `memo` は使用しない ことにする


## code block file name

code block での file name の書きかた

```json title="example.json"
{
  key01 : "val01",
  key02 : "val02"
}
```



