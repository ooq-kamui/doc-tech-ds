
# podman network


- network は docker のやりかた?
- podman の場合は pod でやる?


## ref

https://reafnex.net/it/it-container/how-to-podman-network/


## network list

```
podman network ls
```


## 詳細 表示

```
podman network inspect <network-name>
```


## network の作成

```
podman network create <network-name>
```


### default value

```
"driver": "bridge",
"subnets": [
  {
    "subnet" : "10.89.0.0/24",
    "gateway": "10.89.0.1"
  }
],
```


## subnet, gateway を指定して network を作成

ex

```
podman network create --subnet=192.168.100.0/24 --gateway=192.168.100.254 <network-name>
```


## container と network を紐づける

```
network connect <network-name> <container-name>
```


## container を起動時に, network を指定する

ex

```
podman run -dt --name cnt-alm-01 --net net-02 almalinux
```

確認

```
podman exec -it cnt-alm-01 /bin/bash
```

container 内で

```
hostname -i
```


## network と ip address を指定して container を起動する

ex

```
podman run -it -d --net net-02 --ip=192.168.100.20 --rm --name cnt-alm-002 almalinux:latest
```

確認

```
po exec -it cnt-alm-002 /bin/bash
```

container 内で

```
hostname -i
```


## container 間の通信を確認する

ex

cnt-alm-01 に入る

```
podman exec -it cnt-alm-01 /bin/bash
```

wip:


## network を削除する

```
podman network rm <network-name>
```


## notice

- podman は 異なる subnet でも通信できる




