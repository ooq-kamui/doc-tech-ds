
# image  -  podman


## image list

```
podman images
```

or

```
podman image list
```


## image を 削除

```
podman rmi <image-name>
```


## save

image を file に書き出す

file は tar で 書き出される

```
podman save -o <file-name> <image-name>
```


## load

image file から image を読み込む

```
podman load xxx
```












