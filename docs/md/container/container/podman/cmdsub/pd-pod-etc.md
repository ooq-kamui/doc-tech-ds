
# podman pod


## basic

- pod は container を 複数 入れられる 入れもの と考えるのがイメージしやすい
- 1つ の pod の中にある 複数の container は localhost で つながっている
  - https://docs.redhat.com/ja/documentation/red_hat_enterprise_linux/9/html/building_running_and_managing_containers/proc_communicating-between-two-containers-in-a-pod_assembly_communicating-among-containers


## pod list

```
podman pod ls
```


## pod の作成

```
podman pod create -p 8080:80 <pod-name>
```

infra container も自動的にできる

確認

```
podman ps
```


## pod の削除

```
podman pod rm <pod-name>
```


## pod の停止

```
podman pod stop <pod-name>
```


## pod の起動

```
podman pod start <pod-name>
```


## pod の再起動

```
podman pod restart <pod-name>
```


