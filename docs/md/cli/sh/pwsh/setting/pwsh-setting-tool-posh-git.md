
# posh-git


## install

```
Install-Module posh-git -Scope CurrentUser -Force
```

profile に下記を追加

```
Import-Module posh-git
```

pwsh restart


## prompt

ex

```
function prompt {
  # "PS " + $( get-location ) + "> "
  $brnch = ( Write-VcsStatus )

  if ($brnch){
    $brnch.Trim() + " "
  }else {
    "_ "
  }
}
```


