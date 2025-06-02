
# podman network macvlan


途中まで実施したものの,  
network は docker の やりかたで,  
podman では pod でやる らしい

podman のやりかたを学びたい場合は, network でやるのは もう古いかも..


## ref

https://reafnex.net/it/it-container/podman_macvlan/


## basic

外から container に通信する 話

macvlan は root mode でしかできないので注意


## macvlan の network を作成

ex

```
podman network create --driver macvlan --subnet=192.168.11.0/24 --gateway=192.168.11.254 -o parent=enp0s25 network-macvlan-001
```

確認

```
podman network inspect network-macvlan-001
```

検証用の container を作成する

Containerfile

```
FROM docker.io/library/almalinux:latest

USER root

RUN echo root:roottest | chpasswd
RUN groupadd -g "1000" "test"
RUN useradd -u "1000" -g "test" -s /bin/bash testuser
RUN echo testuser:test0000 | chpasswd
RUN dnf -y install openssh-server; dnf -y install openssh-clients; dnf -y install rsyslog; dnf clean all
RUN echo "Port 2222" >> /etc/ssh/sshd_config
RUN systemctl enable rsyslog
```

```
podman build -t macvlan-alm-001:1.0.0 -f Containerfile .
```

macvlan の network を設定して, 上記 の image から container 作成

かつ, ip address 指定

```
podman run -d -it --rm --net network-macvlan-001 --ip=192.168.11.1 --name cntinr-macvlan-alm-001 macvlan-alm-001:1.0.0 /sbin/init
```

確認

```
podman exec -it cntinr-macvlan-alm-001 /bin/bash
```

自分の環境では,
その後の 確認ができず.. 留保






