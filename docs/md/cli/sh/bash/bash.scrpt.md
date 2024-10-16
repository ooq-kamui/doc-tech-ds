
# bash script scrpt


## arg

### all

```
echo "$@"
```


## test cmd

### path があるか

```
if test -e ./file_path
then
```

### file があるか

```
if test -f ./file_path
then
```

### dir があるか

```
if test -d ./dir
then
```

### ln があるか

```
if test -L ./ln_path
then
```

### file が 空 でないか

```
if test -s ./file_path
then
```

### file が書込可能か

```
if test -w ./file_path
then
```

### file が実行可能か

```
if test -x ./file_path
then
```



