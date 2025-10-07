
# faq  -  tree-sitter


## gcc err

次の err とき

```
No C compiler found! "cc", "gcc", "clang", "cl", "zig" are not executable.
```

gcc を install する

### alma

```
sudo dnf install gcc
```

### pwsh

```
scoop install gcc
```


## cert err

zscaler の制約などで, 次の err のとき

```
nvim-treesitter[lua]: Error during download, please verify your internet connection
curl: (60) SSL certificate problem: unable to get local issuer certificate
More details here: https://curl.se/docs/sslcerts.html

curl failed to verify the legitimacy of the server and therefore could not
establish a secure connection to it. To learn more about this situation and
how to fix it, please visit the webpage mentioned above.
```

- dl を curl でなく, git で 行うようにする
- git の dl の際, ssl 証明書の検証をしない設定で dl する


### dl を curl でなく, git で 行うようにする

neovim に 次を設定  

```
require("nvim-treesitter.install").prefer_git = true
```

### git の dl の際, ssl 証明書の検証をしない設定で dl する

git の設定を次のようにする

```
git config --global http.sslVerify false
```

この状態で, TSInstall を実行する


終わったら, 必ず

```
git config --global http.sslVerify false
```

で設定を戻すこと


