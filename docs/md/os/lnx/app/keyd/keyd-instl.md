
# keyd  -  install

https://github.com/rvaiya/keyd

## ref

- https://qiita.com/showchan33/items/56baa1c7a145f14ebf82
- https://zenn.dev/sanmal/articles/fad4d635c2a323


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

- 上記で, 再起動後も自動で起動します


## 起動しているかの確認

```
systemctl status keyd
```


## 自動起動が有効になっているか確認

```
systemctl is-enabled keyd
```


