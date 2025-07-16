
# npm

nodejs の package manager


## install

```
wip:
```

## npm 自体の update

```
npm update -g npm
```


## npm, npx で permission err になるとき

```
sudo npm cache clean --force
```


## `UNABLE_TO_GET_ISSUER_CERT_LOCALLY` の err

```
npm -g config set strict-ssl false
```

```
npm -g config set strict-ssl true
```

確認

```
npm config list
```




