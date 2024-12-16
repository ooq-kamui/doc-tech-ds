
# rsync


## option

```
-a         なるべくコピー元のファイルと同一条件でコピー
-v         詳細を出力
-e         ssh 指定
--delete   転送元にないファイルは削除
--exclude  除外
           対象が複数の場合は --exclude を繰り返す
           sync 元 の相対パスで指定
--dry-run  test 実行
```


## ex

```
set l_dir hugo
set s_dir hugo

rsync -av -e ssh --delete     \
  $l_dir/                     \
  --exclude="data/"           \
  --exclude="test/"           \
  kamui@ooq.jp:~/$s_dir       \

#  --dry-run                   \
```


## local dir どうしでも可

```
set dev_dir docs01
set rel_dir docs02

rsync -av --delete \
  $dev_dir/        \
  $rel_dir         \
```


## faq

```
bash: line 1: rsync: command not found
```

相手側に rsync が install されていない

```
dnf install rsync
```



