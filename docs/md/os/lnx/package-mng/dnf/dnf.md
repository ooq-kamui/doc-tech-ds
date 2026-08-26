
# dnf


## dnf 自体の install

- redhat 系 の時点で dnf は install されています


## dnf 自体の upgrade ( update )

```
sudo dnf upgrade dnf
```


## app の install

```
sudo dnf install <app-name>
```


## app の upgrade ( update )

```
sudo dnf upgrade <app-name>
```


## community project repository を enable にする

```
sudo dnf copr enable <usr/prj>
```

のあと, install

```
sudo dnf install <prj>
```


