
# ln


## symbolic link cre / mod

```
ln -sin <target-path> <link-name>
```


### option

```
i  上書き確認あり
f  上書き確認なし
   i と f を両方書いたときは後ろにあるほうが優先される
```


### case dir

- arg2 の 末尾が 既存の dir_name の場合は,  
  その下に target_path の 末尾の file_name で ln がつくられる
- dir の ln を つくる場合
  - arg1 の 末尾に `/` をつけないのが無難


