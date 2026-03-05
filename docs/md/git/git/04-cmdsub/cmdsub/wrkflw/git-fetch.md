
# git fetch


## 基本

リモートから最新内容をローカルに取り込む

origin/master に取り込まれる

master ではないので注意


master        : local の中心となる統合 branch で, local branch とつながったもの

origin/master : local にある, リモートのmaster branch を追跡する remote 追跡 branch


merge までは行わない



## すべてを取り込む

```
git fetch
```


## `repository : all` を取り込む

```
git fetch --all
```


## `repository : origin`, `branch : all` を取り込む

```
git fetch origin
```


## 特定 branch のみを fetch する

```
git fetch origin <branch-name>
```

fetch を行っただけでは 他人の更新はプログラムへは取り込まれていない

そこまで行うには merge でマージ作業を行う


## tag を取り込む

```
git fetch --tags
```

```
git fetch -t
```


## branch の削除 を取り込む

remote repository から branch が削除されても,
local repository には origin/branch1 といった形で branch が残ります

その場合, 以下のコマンドで branch の削除情報の最新の状態を取り込むことができます

```
git fetch --prune
```

```
git fetch -p
```


## fetch と pull の違いについて

pull は 内部で

- fetch
- merge

を順次実行するコマンドです


