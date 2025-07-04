
# podman exec


## container で cmd 実行する

```
podman exec -it <container-name> <cmd>
```

- `<cmd>` が 
  - `/bin/bash` なら bash で container に入る
  - `psql` なら postgres で container に入る

といったことができる


## option

```
-i    ???


-t    ???


```


## container 内 の bash に入る

```
podman exec -it <container-name> /bin/bash
```


## container 内 の postgres に入る

```
podman exec -it <container-name> psql -U <usr-name> -d <db-name>
```



