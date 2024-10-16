
# git push


## 基本

local commit history を remote に反映する

commit history が local と同じになる

```
git push origin main
```

`origin` は `remote_ref` のこと


branch 名 省略も可

```
git push origin
```

( 指定するほうが無難 かどうかは微妙なところ )


origin 省略も可

```
git push
```

( 指定するほうが無難 かどうかは微妙なところ )



基本は 同 branch で行う

別 branch への push はやらないのが 無難,
混乱のもと なので

同 branch へ push & pull req でやる



## 別の branch に push する

どうしてもやりたい場合のみ

```
git push origin <local_branch_name>:<remote_branch_name>
```

`:` は省略できないので注意

`:` 前を省略すると 空 push ( branch 削除 ) になってしまうので 注意



