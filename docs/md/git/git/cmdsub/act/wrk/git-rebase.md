
# git rebase

ref

https://qiita.com/C_HERO/items/06669621a1eb12d8799e


## desc

- rebase は merge ( 広義 ) の 一種です
  - ここで merge ( 広義 ) とは  
    他 branch ( 通常は remote branch ) にある まだ取り込んでいない commit を  
    自 branch ( local branch ) に取り込む  
    のこと


## 基本

```
git rebase origin/<branch-name>
```


## rebase の挙動

- local branch の 未 push commit をいったん棚上げする
  - commit が取り消され, file の変更内容は stash されたような状態になる
- remote branch の 未取り込みの commit を first forward で取り込む
- conflict がない場合
  - commit id は 新 commit id がつく
  - commit msg はもとのまま
  - commit 時間 ( commit history の時系列 ) はもとのまま
  - もとの commit id は commit history から 消える
- conflict がある場合
  - rebase 処理としては rebase 中 の状態になる
    - stash pop で conflict があったときのような状態 になる
  - 手動で conflict を解消する
  - `git rebase --continue` で rebase 処理を再開
    - file の変更内容は 新 commit として commit される
      - commit id は 新 commit id がつく
      - commit msg はもとのものから変更もできる
      - commit 時間 はもとのまま
        - 自 commit 時間 のほうが前だった場合
          - commit 順は 自 commit のほうが あとになるので,  
            commit 時間 と commit 順 が一致しないものとなる
      - もとの commit id は commit history から 消える


### image

```
befor
                 sync
                 |
  remote : c1 - c2 - c5 - c6
                 |
  local  : c1 - c2 - c3 - c4

after
                           sync
                           |
  remote : c1 - c2 - c5 - c6
                           |
  local  : c1 - c2 - c5 - c6 - c3' - c4'
  
                     c3   c4 はなくなる
```

## option

### `--continue`

conflict 解消後に 続きの rebase 処理を行う

```
git rebase --continue
```


### `--interactive`

```
-i  --interactive
```


## q

- stash するのと何が違うのか


## `git pull --rebase`

```
git pull --rebase
```

は

```
wip:
```

と同じ



