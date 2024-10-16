
# aws-cli


## install

### cloud9

初めから install されている


### mac

ref  
https://docs.aws.amazon.com/ja_jp/cli/latest/userguide/getting-started-install.html

```
curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
```

```
sudo installer -pkg AWSCLIV2.pkg -target /
```


## aws configure ( config )

### 確認

```
aws configure list
```

`amplify configure` で設定していれば, そちらと同じかもしれない ? ( 未確認 )


### 設定

```
aws configure
```

cloud9 の場合は
とくに自分で 設定 しなくてもいい はず ( 基本的には )



