
# postgres  -  install  -  ec2


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

wip:

ref url


