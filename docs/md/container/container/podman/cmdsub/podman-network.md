
# podman network


実施してみたものの, network は docker のやりかたらしく,  
podman の場合は pod でやるそう

podman でのやりかたを学びたい場合は, このやりかたは もう古いかも .. しれません



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

### basic

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


### subnet, gateway を指定して network を作成

ex

```
podman network create --subnet=192.168.100.0/24 --gateway=192.168.100.254 <network-name>
```


## network を指定して container を起動する

ex

```
podman run -it -d --net network002 --rm --name container-alm-001 almalinux:latest
```

確認

```
podman exec -it container-alm-001 /bin/bash
```

container 内で

```
hostname -i
```


## network と ip address を指定して container を起動する

ex

```
podman run -it -d --net network002 --ip=192.168.100.20 --rm --name container-alm-002 almalinux:latest
```

確認

```
po exec -it container-alm-002 /bin/bash
```

container 内で

```
hostname -i
```


## container 間の通信を確認する

ex

container-alm-001 に入る

```
podman exec -it container-alm-001 /bin/bash
```


## network を削除する

```
podman network rm <network-name>
```


## notice

- podman は 異なる subnet でも通信できる




