
# git pull

ref

https://tracpath.com/docs/git-pull/


## basic

ex

```
git pull origin main
```

git pull は, 次の コマンドを一度にやることです

```
git fetch origin main

git merge FETCH_HEAD
```

補足

```
FETCH_HEAD : fetch した remote の 同 branch の 最新 commit
```


### `--rebase` option

merge の替わりに rebase を行う

```
--rebase[=false|true|merges|preserve|interactive]

false        現在のブランチをアップストリームブランチにマージします

true         フェッチ後に現在のブランチをアップストリームブランチの上にリベースします
             アップストリームブランチに対応するリモート追跡ブランチがあり
             アップストリームブランチが最後にフェッチされてからリベースされた場合
             リベースはその情報を使用して、非ローカル変更のリベースを回避します

merges       git rebase --rebase-merges を使用してリベースし
             ローカルマー ジコミットがリベースに含まれるようにします

preserve     非推奨
             ローカルで作成されたマージコミットがフラット化されないように
             --preserve-mergesオプションをgit rebase にパスしてリベースします

interactive  リベースのインタラクティブモードを有効にします
```

これの default を config で設定しておける

ex

```
[pull]
  rebase = false
```

- rebase で conflict が起きたときの対処法は rebase を参照


## option

その他の option

```
wip:
```



## git pull -f ( 強制 ) はありません

そのようなときは, 次のコマンドを実行します

remote 最新を取得

```
git fetch origin main
```

local main を remote の main に強制的に合わせる

```
git reset --hard origin/main
```


`git push -f` で強制的に remote を変更したあと,
別の local で上記を行う ことになる


## faq

### local の現在の branch と pull で指定した branch が違うとどうなる?


