
# podman run pod


## 指定の pod で container を起動する

ex

```
podman run -d --pod pod-nginx nginx:latest
```


## 稼働している pod から pod の yaml を作る

```
podman kube generate -f <file-name> <pod-name>
```

ex

```
podman kube generate -f pod-nginx.yaml pod-nginx-001
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


## pod の yaml file から pod を作る

ex

```
podman kube play --net <macvlan-name> --ip <192.168.11.200> <yaml-file>
```

ex

```
podman kube play --net macvlan-001 --ip 192.168.11.200 pod-nginx.yaml
```


