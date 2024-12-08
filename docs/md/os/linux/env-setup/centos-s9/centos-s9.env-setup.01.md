
# centos stream 9  -  env setup part 01  -  ( sakura vps )


## git

```
sudo dnf -y install git
```


## ruby

```
sudo dnf module -y install ruby:3.3/common
```


## brew

bash にて

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

```
(echo; echo 'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"') >> /home/centos/.bashrc
```

```
eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"
```


## tar

```
sudo dnf install tar
```


## noevim

```
brew install neovim
```


## fish

```
brew install fish
```

install は success したように見える, が

```
fish
```

で, 下記の err

```
fish: error while loading shared libraries: libstdc++.so.6: cannot open shared object file: No such file or directory
```

`libstdc++.so.6` が どの package に入っているかを調べる

```
yum whatprovides */libstdc++.so.6
```

念のためレベルで 32bit and 64bit とも install

```
sudo yum install libstdc++.i686
```

```
sudo yum install libstdc++.x86_64
```

err 解消されない

share lib path を確認

```
sudo ldconfig -p | grep stdc
```

or

```
sudo ldconfig -v
```

問題なさそう

cache clear

```
sudo ldconfig
```

解消されない

```
cat /etc/ld.so.conf
include ld.so.conf.d/*.conf
```

```
ll /etc/ld.so.conf.d/
total 0
```

こちらは 確かに 空である..

では `sudo ldconfig -v` `sudo ldconfig -p` の表示は何なのか..?

try

上記の設定

それでもダメなら

`LD_LIBRARY_PATH` を設定してみる

```
LD_LIBRARY_PATH=/lib64
```

```
export LD_LIBRARY_PATH
```

上記は解消

次の err

```
fish: /lib64/libstdc++.so.6: version `GLIBCXX_3.4.30' not found (required by fish)
```

状況確認

```
strings /lib64/libstdc++.so.6 | grep GLIBCXX
```

確かに
`GLIBCXX_3.4.30' はない

gcc を src から build することにする

```
cd /usr/local/src
```

```
sudo yum install gcc
```

```
sudo yum install gcc-c++
```

確認

```
ll /lib64/libstdc++.so.6*
```

```
lrwxrwxrwx 1   19 2023-12-20 01:17 /lib64/libstdc++.so.6 -> libstdc++.so.6.0.29
-rwxr-xr-x 1 2.3M 2023-12-20 01:21 /lib64/libstdc++.so.6.0.29
```

```
sudo curl -LO http://ftp.tsukuba.wide.ad.jp/software/gcc/releases/gcc-14.2.0/gcc-14.2.0.tar.gz 
```

```
sudo curl -LO http://ftp.tsukuba.wide.ad.jp/software/gcc/releases/gcc-14.2.0/sha512.sum 
```

```
sha512sum --check sha512.sum 
```

```
sudo tar xzfv gcc-14.2.0.tar.gz 
```

```
cd gcc-14.2.0
```

```
sudo ./contrib/download_prerequisites
```

err

```
./contrib/download_prerequisites: line 269: bzip2: command not found
```

```
sudo yum install bzip2
```

try re

```
sudo ./contrib/download_prerequisites                                                
```

```
./contrib/download_prerequisites: line 53: type: wget: not found
gettext-0.22.tar.gz: OK
gmp-6.2.1.tar.bz2: OK
mpfr-4.1.0.tar.bz2: OK
mpc-1.2.1.tar.gz: OK
isl-0.24.tar.bz2: OK
All prerequisites downloaded successfully.
```

ver 確認

```
gcc --version
```

```
gcc (GCC) 11.4.1 20231218 (Red Hat 11.4.1-3)
Copyright (C) 2021 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```

build

```
mkdir build
```

```
cd build
```

```
sudo ../configure --enable-languages=c,c++ --prefix=/usr/local --disable-bootstrap --disable-multilib
```

```
sudo make
```

ここで時間かかる

```
g++: fatal error: Killed signal terminated program cc1plus
compilation terminated.
```

メモリ不足 らしき

上記が success だったら, 次は 下記 cmd, .. なのだが

```
sudo make install
```

scl で install してみる

```
sudo yum install -y centos-release-scl
```

centos stream 9 では 使えない ぽい

swap を設定してみる

ref :
https://aulta.co.jp/technical/server-build/centos-stream-9/swap-memory

確認

```
top
```

```
free -m
```

スワップファイルを作成

```
sudo fallocate -l 1G /swapfile
```

権限を設定

```
sudo chmod 600 /swapfile
```

スワップファイル をスワップ領域として設定

```
sudo mkswap /swapfile
```

スワップファイル を有効にする

```
sudo swapon /swapfile
```

有効になったことを確認

```
swapon --show
```

スワップファイルを永続化する

```
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
```

build re

```
sudo ../configure --enable-languages=c,c++ --prefix=/usr/local --disable-bootstrap --disable-multilib
```

```
sudo make
```

進んだようではある

ここまでやって, 下記に, 
brew install 時での それらしきものがあるのに気づく,

```
ll /home/linuxbrew/.linuxbrew/Cellar/gcc/14.1.0_2/lib/gcc/current/libstdc++.so.6* 

lrwxrwxrwx 1   19 2024-05-07 16:20 /home/linuxbrew/.linuxbrew/Cellar/gcc/14.1.0_2/lib/gcc/current/libstdc++.so.6 -> libstdc++.so.6.0.33
-r-xr-xr-x 1 2.8M 2024-07-29 05:00 /home/linuxbrew/.linuxbrew/Cellar/gcc/14.1.0_2/lib/gcc/current/libstdc++.so.6.0.33
-r--r--r-- 1 2.4K 2024-05-07 16:20 /home/linuxbrew/.linuxbrew/Cellar/gcc/14.1.0_2/lib/gcc/current/libstdc++.so.6.0.33-gdb.py
```

こちらに path を通せばいけるのでは という気はする..


が, ここまでやったので, make からの install を 続行 してみる

```
sudo make install
```

success のよう

`/usr/local/lib64/` にいろいろ build, install されている

```
ll /usr/local/lib64/libstdc++.so.6* 
lrwxrwxrwx 1   19 2024-08-15 17:55 /usr/local/lib64/libstdc++.so.6 -> libstdc++.so.6.0.33
-rwxr-xr-x 1  20M 2024-08-15 17:55 /usr/local/lib64/libstdc++.so.6.0.33
```

`/usr/local/lib64/` に path を通す

```
LD_LIBRARY_PATH=/usr/local/lib64
```

```
export LD_LIBRARY_PATH
```

try

```
fish 

Welcome to fish, the friendly interactive shell
Type help for instructions on how to use fish
centos@os3-304-41716 /u/l/s/g/build>
```

ok !!  done !!


`/usr/local/src/` 配下を削除するのを忘れないように



go to part 2



