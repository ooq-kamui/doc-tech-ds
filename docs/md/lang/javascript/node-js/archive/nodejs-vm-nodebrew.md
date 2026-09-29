
# nodebrew

nodejs の version manager


## install


### brew で nodebrew を install

```
brew install nodebrew
```

msg の最後に表示される cmd を実行して,
path を通すなど すること,
bash で install するのが 無難,
fish だと err になる

確認

```
nodebrew -v
```

バージョンが表示されればOK

環境変数を追加

```
vi ~/.bash_profile
```

で, 以下を追加する

```
export PATH=$HOME/.nodebrew/current/bin:$PATH
```

bash_profileを更新して設定を反映させる

```
source ~/.bash_profile
```

セットアップ

```
nodebrew setup
```


### nodebrew で nodejs を install

```
nodebrew install latest
```


### バージョン指定してnodeをインストールする

#### インストール可能なバージョンを確認

```
nodebrew ls-remote
```

#### nodeのインストール

```
nodebrew install-binary <version>
```

nodejs, npm が install される


### nodebrew で nodejs の ver list 確認

```
nodebrew ls
```

```
v.16.6.0
```


### nodebrew で nodejs の ver 指定

```
nodebrew use v16.6.10
```


### nodebrew で nodejs を uninstall, ver 指定

```
nodebrew uninstall vxx.x.xx
```


### npm が使えなくなったとき

path が通っていなくなった可能性がある

path の confirm

npm の install dir

通常は下記

```
~/.nodebrew/current/bin/
```

上記はあるが
具体的な current_ver の dir 配下に npm がない
という現象が起きる
このときは, use ver を npm が存在する ver に指定し直して対応した



