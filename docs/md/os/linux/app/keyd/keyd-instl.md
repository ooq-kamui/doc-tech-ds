

# keyd

https://github.com/rvaiya/keyd

## ref

- https://qiita.com/showchan33/items/56baa1c7a145f14ebf82
- https://zenn.dev/sanmal/articles/fad4d635c2a323


## keyd とは

- keyd は linux の kernel レベル ( evdev ) で動くキーリマップデーモン
- x11 / wayland / tty を問わず, システム全体で動作する
- kde wayland でも使える

[rvaiya/keyd - GitHub](https://github.com/rvaiya/keyd )


## install

Fedora 向けには copr パッケージが提供されています

### copr repository を有効化

```bash
sudo dnf copr enable alternateved/keyd
```

### install

```
sudo dnf install keyd
```


## 起動

```bash
sudo systemctl enable --now keyd
```

これで keyd が常駐し, 再起動後も自動で起動します


