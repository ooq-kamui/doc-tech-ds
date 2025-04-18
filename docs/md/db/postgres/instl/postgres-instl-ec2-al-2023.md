
# postgres  -  install  -  amazon linux 2023


## install

ref
https://www.cloudbuilders.jp/articles/1108/

wip:


## パッケージインストール

```
sudo dnf install postgresql16-server
```


## PostgreSQLの初期化

```
sudo postgresql-setup initdb
```


## pw

```
sudo passwd postgres
```


## サービス起動

```
sudo systemctl start postgresql
```


## 自動起動

```
sudo systemctl enable postgresql
```


