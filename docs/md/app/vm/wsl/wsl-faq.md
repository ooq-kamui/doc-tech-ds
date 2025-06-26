
# wsl  -  faq


## zscaler で err

### npm install err

```
env : almalinux10 ( hed hat 系 )
```

#### err

```
_ npm install
npm error code 1
npm error path /home/alm/wrk/prj/xxx/node_modules/sharp
npm error command failed
npm error command sh -c (node install/libvips && node install/dll-copy && prebuild-install) || (node install/can-compile && node-gyp rebuild && node install/dll-copy)
npm error sharp: Downloading https://github.com/lovell/sharp-libvips/releases/download/v8.14.5/libvips-8.14.5-linux-x64.tar.br
npm error sharp: Via proxy http://tyo4.sme.zscaler.net: no credentials
npm error sharp: Please see https://sharp.pixelplumbing.com/install for required dependencies
npm error sharp: Installation error: unable to get local issuer certificate
npm error A complete log of this run can be found in: /home/alm/.npm/_logs/2025-06-24T04_35_07_421Z-debug-0.log
```

#### resolve

ファイル名を指定して実行 ( win + r ) で `certmgr.msc` を実行

`証明書 - 現在のユーザー > 信頼されたルート証明書 > 証明書 > Zxcaler Root CA`

を export

```
type      : Base 64 encoded X.509 (.CER)
file name : zscaler.cer
```

`cer > crt` に変換

```
openssl x509 -inform PEM -in zscaler.cer -out zscaler.crt
```

crt を所定の dir に配置

almalinux ( red hat 系 ) は下記

```
sudo cp zscaler.crt /usr/share/pki/ca-trust-source/anchors/zscaler.crt
```

反映

```
sudo update-ca-trust extract
```

`.bashrc` に 環境変数を追加

```
export NODE_EXTRA_CA_CERTS=/usr/share/pki/ca-trust-source/anchors/zscaler.crt
```

立ち上げなおした bash で

```
npm install
```

で, いけるはず


#### ref

- https://qiita.com/ichi-ken/items/5a04a732524c72ff809a
- https://zenn.dev/qmotas/scraps/d0332caff19453
- https://docs.redhat.com/ja/documentation/red_hat_enterprise_linux/9/html/securing_networks/adding-new-certificates_using-shared-system-certificates


