
# wsl distro


## install されている distro を表示

```
wsl --list --verbose
```

- state も確認できる

ex

```
_ wsl --list --verbose
  NAME                      STATE           VERSION
* AlmaLinux-10              Running         2
  Ubuntu                    Stopped         2
  podman-machine-default    Stopped         2
_ 
```


## install できる distro を表示

```
wsl --list --online
```


## distro を install

```
wsl --install -d <distro>
```


## distro を del

```
wsl --unregister <distro>
```


## 同じ distro を 複数 install

### すでに使っている distro と 同じ distro を 新規に作成したい場合

- 通常 distro name は 所定の default の名前がついている
  - ex `AlmaLinux-10`
- 現在使用している distro を 別名にする
  - 現状 これは export, import で 複製し,  
    もとのほうを 削除 でやるしかない ( と思われる )
  - export する
  - import する
    - このとき, distro name に 別名をつける
  - 複製された distro に login して, 動作確認する
  - もとの distro を削除する  
    ( default の distro name のほうのこと )
- 改めて, まっさらな distro を install
  - これは再び, default の distro name で作成される
  - ディスク容量があるなら,  
    この時点のまっさらな distro の tar を import して補完しておくとよい  
    再度, まっさらな環境がほしくなったときの 手順が早まる
- これで, 同じ distro が 2つ できたはず


## wsl に login したとき, su になる

- これを回避する方法
- この現象は import した distro で起きる
- distro 環境の中の 下記の file を編集
- wsl 再起動

```conf title='/etc/wsl.conf'
[user]
default=<user-name>
```




