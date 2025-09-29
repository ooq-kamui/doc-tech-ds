
# if


## ref

https://learn.microsoft.com/ja-jp/powershell/scripting/learn/deep-dives/everything-about-if?view=powershell-7.4


## structure

```
if      ($flg01){

}elseif ($flg02){

}else{

}
```


## cnd

### or

```
if ($val01 -or $val02){

}
```


### and

```
if ($val01 -and $val02){

}
```


### not

```
if (-not $val01){

}
```


### test

```
-eq    =   等しい      大文字小文字が区別されない
-ieq   =   等しい      大文字小文字が区別されない
-ceq   =   等しい      大文字小文字が区別される  

-ne    !=  等しくない  大文字小文字が区別されない
-ine   !=  等しくない  大文字小文字が区別されない
-cne   !=  等しくない  大文字小文字が区別される  

-gt    >   より大きい
-igt   >   より大きい  大文字小文字が区別されない
-cgt   >   より大きい  大文字小文字が区別される

-ge    >=  以上
-ige   >=  以上        大文字小文字が区別されない
-cge   >=  以上        大文字小文字が区別される

-lt    <   より小さい
-ilt   <   より小さい  大文字小文字が区別されない
-clt   <   より小さい  大文字小文字が区別される

-le    <=  以下
-ile   <=  以下        大文字小文字が区別されない
-cle   <=  以下        大文字小文字が区別される
```

### str null or empty

```
[System.String]::IsNullOrEmpty($var)
```


### var def

```
if ($val -eq $null){

  echo 'var is not def'
}
```


### test path

https://learn.microsoft.com/ja-jp/powershell/scripting/lang-spec/chapter-05?view=powershell-7.4

```
wip:
```


