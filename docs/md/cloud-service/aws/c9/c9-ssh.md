
# aws ssh connect

ref
- https://dekfractal.com/4666.html


## start

cloud9 の環境はあるとする


## aws console

elastic ip setting

- elastic ip create
- relate instance


security group setting

- inbound rule create
  - ssh


key pare create

- key download
  - `~/downloads/key.pem`


## client pc ( mac )

key file mv

```
mv ~/downloads/key.pem ~/.ssh/
```

key file chmod

```
chmod 600 ~/.ssh/key.pem
```

public key ( authorized key ) create & copy

```
ssh-keygen -y -f ~/.ssh/key.pem | pbcopy
```


## cloud9

public key ( authorized key ) setting

```
vi ~/.ssh/authorized_keys
```

最下行に copy した key str を paste


## ssh connect try

at mac

ex

```
ssh ec2-user@ec2-xx-xx-xx-xx.ap-northeast-1.compute.amazonaws.com -i ~/.ssh/key.pem
```

接続が成功したら,
上記を fish script 化 しておけば, 次から 楽



