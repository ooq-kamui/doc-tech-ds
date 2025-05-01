
# lua if cnd


## if

```
if     a == 0 then

  print('a : 0')

elseif a == 1 then

  print('a : 1')

else
  print('else')
end
```


## operator

```
==    等しい
~=    等しくない

not   

and   
or    
```


## 三項演算

```
x = ( cnd ) and val1 or val2
```


## not の解釈で注意

```
if not val1 == val2 then
-- と書くと
-- if (not val1) == (val2) then -- と評価される
-- if not (val1 == val2) then   -- ではないので注意
```


