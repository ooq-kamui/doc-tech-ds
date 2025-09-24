
# tree-sitter


## basic

```
wip:
```


## TSInstall

```
wip:
```


## faq

### TSInstall で err

```
nvim-treesitter[lua]: Error during download, please verify your internet connection
curl: (60) SSL certificate problem: unable to get local issuer certificate
More details here: https://curl.se/docs/sslcerts.html

curl failed to verify the legitimacy of the server and therefore could not
establish a secure connection to it. To learn more about this situation and
how to fix it, please visit the webpage mentioned above.
```

のとき

neovim に 次を設定  

```
require("nvim-treesitter.install").prefer_git = true
```

dl を git で行うようになる

git の設定を次のように設定する

```
git config --global http.sslVerify false
```

ssl 証明書検証しない で dl するようになる

この状態で, TSInstall を実行する


終わったら, 必ず

```
git config --global http.sslVerify false
```

で設定を戻すこと



