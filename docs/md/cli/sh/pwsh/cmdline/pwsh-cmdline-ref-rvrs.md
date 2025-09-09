
# pwsh  ref-rvrs


## file path の出力を file path のみにする

`conver-path`

ex

```
pwd | convert-path
```


## `tail -f`

```
Get-Content -Path <file_path> -Wait -Tail <line_num> -Encoding UTF8
```

- win の pwsh から wsl の file を 上記で見ようとすると err で見れない現象あり
  - wsl 上の file であれば, wsl ( linux ) から `tail -f` できるはずなので, そうすれば ok のはず





