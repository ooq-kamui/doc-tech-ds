
# centos stream 9  -  env setup part 03  -  ( sakura vps )


## node

```
dnf module list nodejs
```

```
sudo dnf module reset nodejs
```

```
sudo dnf module -y enable nodejs:18
```

```
sudo dnf module -y install nodejs:18/common
```


## docusaurus

既存の docusaurus dir に cd して

下記で必要なものは自動的に install される

```
npm install
```

```
npm run build
```



