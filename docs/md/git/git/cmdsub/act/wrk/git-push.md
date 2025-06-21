
# git push


## 基本

local commit history を remote に反映する

commit history が local と同じになる

```
git push origin main
```

`origin` は `remote_ref` のこと



基本は remoto と local 同 branch で行う

別 branch への push はやらないのが 無難,
混乱のもと なので


## 引数を省略した場合

setting によって挙動 が変わる
( 挙動を決められる )

ref

https://qiita.com/westhouse_k/items/167276ece3b9562eee3e

https://k-koh.hatenablog.com/entry/2020/02/04/114557


### 現在の設定の確認

```
git config --global push.default
```

### 設定する

```
git config --global push.default setting_val
```

設定できる値

```
nothing   何もプッシュしない
current   現在のブランチを同名リモートブランチとしてプッシュする
upstream  現在のブランチの上流ブランチにプッシュする
simple    現在のブランチを同名の上流ブランチにプッシュする
matching  すべてのローカルブランチを同名のブランチにプッシュする
```

ex

```
git config --global push.default current
```


### 確認

```
git config --list
```

### branch 名 省略

ex

```
git push origin
```

### origin から 省略

ex

```
git push
```


## 別の branch に push する 場合

どうしてもやりたい場合のみ

```
git push origin <local_branch_name>:<remote_branch_name>
```

`:` は省略できないので注意

`:` 前を省略すると 空 push ( branch 削除 ) になってしまうので 注意



