
# github  -  faq


## git push  -  err

git push 時に, password は使えない err が出たとき

err

```
remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
fatal: Authentication failed for 'https://github.com/ooq-kamui/cnf.git/'
```


### slove

#### slove 1

- github で access token を取得
- git remote で access token を設定

```
git remote set-url origin https://access-token@github.com/ooq-kamui/doc-tech-ds
```


#### slove 2

- github で access token を取得
- access token を config に 設定 する

```
git config --local credential.helper store
```


#### slove 3

- github で access token を取得
- git push の password の画面で access token を入力する

この方法の場合, 毎回 実施する必要がある


### ref

https://docs.github.com/ja/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens

https://dev.classmethod.jp/articles/github-personal-access-tokens/



## remote の branch 名 を master > main に変更

github の gui 上から変更する





