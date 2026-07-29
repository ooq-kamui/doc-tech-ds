
# ln


## symbolic link cre / mod

```
ln -sin target_path link_name
```

### case dir

- arg2 の 末尾が 既存の dir_name の場合は,  
  その下に target_path の 末尾の file_name で ln がつくられる
- dir の ln を つくる場合
  - arg1 の 末尾に `/` をつけないのが無難


