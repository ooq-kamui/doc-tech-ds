
# ssh key gen


## key type

- ed25519
  - いま ( 2025 ) はこちらを推奨
- rsa
  - 最低 4096 bit


## ed25519

### key gen

```
ssh-keygen -t ed25519 -C "email-address"
```

任意の dir で実行しても, `~/.ssh` の配下に作成される

ex

```
_ ssh-keygen -t ed25519 -C "ooq.tiki@gmail.com"
Generating public/private ed25519 key pair.
Enter file in which to save the key (/home/ec2/.ssh/id_ed25519):
Enter passphrase for "/home/ec2/.ssh/id_ed25519" (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/ec2/.ssh/id_ed25519
Your public key has been saved in /home/ec2/.ssh/id_ed25519.pub
The key fingerprint is:
SHA256:------------------------------------------- ooq.tiki@gmail.com
The key's randomart image is:
+--[ED25519 256]--+
|                 |
|                 |
+----[SHA256]-----+
_
_ ll ~/.ssh/
total 28K
-rw------- 1  411 2025-08-25 09:09 id_ed25519
-rw-r--r-- 1  100 2025-08-25 09:09 id_ed25519.pub
```

file name を適当に rename して保管しておく

`id_ed25519` を 他 svr へ cp などする場合は, permission を上記とすること


### key pub set

接続先 svr で

`id_ed25519.pub` の内容を
`~/.ssh` の中の
`authorized_keys` に追加する


ssh login するときに `id_ed25519` を使用する


## private key から public key を作成する

- aws などで, private key のみ作成した場合  
- private key から public key を抽出できます

```
ssh-keygen -y -f xxx.pem
```







## ref

https://zenn.dev/tko_kasai/articles/326d8104278c0b


