
# mysql


## 新しくユーザーを作成する

```
CREATE USER 'your_name'@'localhost' IDENTIFIED BY 'your_password';
```


## 作成したユーザーに作成したデータベースの操作権限を付与する

```
GRANT ALL PRIVILEGES ON database_name.* TO 'your_name'@'localhost';
```


## 設定を反映する

```
FLUSH PRIVILEGES;
```


## .mylogin.cnf を使用して mysql に login する

```
mysql --login-path=local fe_fu
```

```
kamui / _____
```


## table list

```
show tables;
```


## dump

```
mysqldump -u USER_NAME -p -h HOST_NAME DB_NAME > OUTPUT_FILE_NAME
```

dump 時の 文字コードの指定 option

```
--default-character-set=utf8
```

ex

```
mysqldump -u USER_NAME -p -h HOST_NAME DB_NAME --default-character-set=utf8 > OUTPUT_FILE_NAME
```


## 文字コードの確認

```
show variables like '%char%';
```


## database の文字コード確認

```
show create database [database_name]
```


## table の文字コード確認

```
show create table [table_name];
```


## select 結果を file 出力

```
SELECT フィールド名 FROM テーブル名 INTO OUTFILE 'ファイル名'
```


## リダイレクトによる file 出力

```
shell> echo 'SELECT * FROM test' | mysql -u root -p test > /tmp/test.dmp
Enter password: 
shell> cat /tmp/test.dmp
id  name
1   isono
2   fu"guta
```



