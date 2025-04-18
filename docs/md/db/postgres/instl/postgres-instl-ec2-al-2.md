
# postgres  -  install  -  amazon linux 2


## ref

https://zenn.dev/kuuki/articles/aws-ec2-install-postgresql


## install

install できる ver 確認

```
amazon-linux-extras list | grep postgresql
```

install

```
sudo amazon-linux-extras install -y postgresql14
```

package も install するのが無難

```
sudo yum install -y postgresql-server postgresql-devel postgresql-contrib postgresql-docs
```

確認

```
psql -V
```


## init

```
sudo postgresql-setup initdb
```

確認

```
sudo cat /var/lib/pgsql/initdb_postgresql.log
```


## 起動

```
sudo systemctl start postgresql
```

確認

```
systemctl status postgresql
```

`Active: active (running)` となっていれば ok


## 自動起動

```
sudo systemctl enable postgresql
```

確認

```
systemctl is-enabled postgresql
```

`enabled` と表示されれば ok


## user postgres の setting

### pw

```
sudo passwd postgres
```

### sudo 権限 付与

```
sudo visudo -f /etc/sudoers.d/cloud-init
```

下記を記述する

```
postgres ALL = (ALL) ALL
```


### db の user postgres の pw

上記の unix account の postgres とは違うものです

unix user postgres に切り替える

```
su - postgres
```

pw 入力して, 上記 user に切り替える

db の user postgres の pw setting

```
psql -c "ALTER USER postgres PASSWORD 'pw_str';"
```


### setting file

user postgres で実行


#### postgres に接続できる ip address の設定

```
/var/lib/pgsql/data/postgresql.conf
```

以下２つのパラメータを確認します

`listen_addresses` : postgres に接続できる ip address

すべての IP から受け付ける場合には `*`

```
listen_addresses = '*'
```


#### server ip address ごと 認証方法 設定

postgres 認証方式

- peer
  - os 側のユーザー名がデータベース側のものと一致している場合のみ 接続を許可
  - ローカルからの接続にのみ 適用可能
- ident
  - クライアントのユーザー名がデータベース側のものと一致している場合のみ 接続を許可
- md5
  - ログイン時にパスワードを使用して 接続を許可
  - `-U` で db のユーザーを指定しない場合は os やクライアントのユーザー名を使用

ref https://www.javadrive.jp/postgresql/ini/index2.html

```
/var/lib/pgsql/data/pg_hba.conf
```

を編集

local の 他 user から access する場合の認証方法, md5 に変更

```
# "local" is for Unix domain socket connections only
#local   all             all                                     peer
local   all             all                                     md5
```

外部から access する場合の認証方法, md5 に変更

```
# IPv4 local connections:
#host    all             all             127.0.0.1/32            ident
host    all             all             0.0.0.0/0           md5
```

postgres 再起動

```
sudo systemctl restart postgresql
```


