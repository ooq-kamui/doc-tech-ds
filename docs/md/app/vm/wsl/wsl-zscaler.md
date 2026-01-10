
# wsl + zscaler


## crt install

### zscaler の crt を export

- win + r で `certmgr.msc` を実行
  - `証明書 - 現在のユーザー > 信頼されたルート証明書 > 証明書 > Zxcaler Root CA`
    を export
    - type      : Base 64 encoded X.509 (.CER)
    - file name : zscaler.cer
    - location  : download など
- file name 変更
  - `mv zscaler.cer zscaler.crt`

### crt を所定の dir に配置 して, 反映

- almalinux ( red hat )

```
sudo cp zscaler.crt /etc/pki/ca-trust/source/anchors/zscaler.crt
```

```
sudo chmod 644 /etc/pki/ca-trust/source/anchors/zscaler.crt
```

```
sudo update-ca-trust
```


## `.bashrc` に 環境変数を追加

### python

wip


### node

```
export NODE_EXTRA_CA_CERTS=/usr/share/pki/ca-trust-source/anchors/zscaler.crt
```

bash launch re

```
npm install
```

で, いけるはず


### ref

- https://knaka20blue.hatenablog.com/entry/2025/01/23/125300
- https://qiita.com/ichi-ken/items/5a04a732524c72ff809a
- https://zenn.dev/qmotas/scraps/d0332caff19453
- https://docs.redhat.com/ja/documentation/red_hat_enterprise_linux/9/html/securing_networks/adding-new-certificates_using-shared-system-certificates


