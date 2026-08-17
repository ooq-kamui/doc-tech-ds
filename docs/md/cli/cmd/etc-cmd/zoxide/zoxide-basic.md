
# zoxide


## ref

https://formulae.brew.sh/formula/zoxide


## remove ( del )

- 既存の jump 先 dir を 消す

```
zoxide remove <path>
```

- ある dir 配下を一括で消す option はない


## faq

### err case

#### `zoxide: unsupported version (got 0, supports 3)`

- ディスクの容量不足 とのこと
  - なのだが, そんなことはないのに出ていた ( 自分は )
- `.local/share/zoxide/db.zo` を削除すると とりあえず直る


