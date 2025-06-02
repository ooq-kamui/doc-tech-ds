
# podman pod


## basic

- pod は container を 複数 入れられる 入れもの と考えるのがイメージしやすい



## pod list

```
podman pod list
```


## pod を作成

```
podman pod create -p 8080:80 <pod-name>
```

infra container も自動的にできる

確認

```
podman ps
```


## 指定の pod 内で, container を起動する

ex

```
podman run -d --pod pod-nginx nginx:latest
```


## 稼働している pod から pod の yaml を生成する

```
podman generate kube -f <file-name> <pod-name>
```

ex

```
podman generate kube -f pod-nginx.yaml pod-nginx-001
```

```
cat pod-nginx.yaml
```

```
# Save the output of this file and use kubectl create -f to import
# it into Kubernetes.
#
# Created with podman-5.5.0
apiVersion: v1
kind: Pod
metadata:
  annotations:
    io.kubernetes.cri-o.SandboxID/cntinr-nginx-001: a864c75be2a5ba528cae6248574cb4354c408a5bfc640990e6803aba55c2b0e0
  creationTimestamp: "2025-06-02T05:18:33Z"
  labels:
    app: pod-nginx-001
  name: pod-nginx-001
spec:
  containers:
  - args:
    - nginx
    - -g
    - daemon off;
    image: docker.io/library/nginx:latest
    name: cntinr-nginx-001
    ports:
    - containerPort: 80
      hostPort: 8080
```


## pod の停止

```
podman pod stop <pod-name>
```


## pod の起動

```
podman pod start <pod-name>
```


## pod の削除

```
podman pod rm <pod-name>
```


## yaml file から pod を再生する

ex

```
podman kube play --net <macvlan-name> --ip <192.168.11.200> <yaml-file>
```

ex

```
podman kube play --net macvlan-001 --ip 192.168.11.200 pod-nginx.yaml
```


