
# ln -s


## ref

https://learn.microsoft.com/ja-jp/powershell/module/microsoft.powershell.management/new-item?view=powershell-7.4


## `$target` へのシンボリックリンクを `$path` として作る

login as admin

```
New-Item -ItemType SymbolicLink -Target $target -Path $path
```

ex

```
New-Item -ItemType SymbolicLink -Target C:\Users\xxx\wrk\prj-pri\dotfiles\nvim\scrpt\lua -Path lua
```

```
New-Item -ItemType SymbolicLink -Target C:\Users\xxx\wrk\prj-pri\dotfiles\nvim\syntax\pwsh -Path syntax
```

```
New-Item -ItemType SymbolicLink -Target C:\Users\xxx\wrk\prj-pri\dotfiles\app\term\wez-term\cnf -Path cnf
```

- `-Target` と `-Path` は 順番はどちらが先でもよい
  - unix の ln と 合わせるなら, `-Target` を先にするほうが 無難 ( 混乱が少ない )
- `-Target` を 指定するときに tab で 自動補完するのが無難
  - 存在の確認
  - win の正確な表記に変換


