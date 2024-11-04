
# chsh


## 基本

login sh を変更する


## 現在 login sh に設定されている sh を確認する

```
echo $SHELL
```


## chsh で 設定可能な list を見る

```
cat /etc/shells
```


## login sh を 変更する

### bash

```
chsh -s /bin/bash
```



