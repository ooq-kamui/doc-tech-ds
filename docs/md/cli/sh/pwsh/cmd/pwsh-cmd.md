
# pwsh cmd


## ls ( ll )

隠しフォルダも表示

```
Get-ChildItem -force
```


## cp

https://learn.microsoft.com/ja-jp/powershell/module/microsoft.powershell.management/copy-item?view=powershell-7.4


cp $file1 $dir2/

```
Copy-Item -Path $file1 -Destination $dir2/
```

cp -r $dir1 $dir2/

```
Copy-Item -Recurse -Path $dir1 -Destination $dir2/
```

cp -f

```
Copy-Item -Force -Path $dir1 -Destination $dir2/
```


## rm

```
Remove-Item $path
```


## zip

### zip

```
Compress-Archive -Path <zip_dir> -DestinationPath <zip_file_path> -Force
```

### zip un

```
Expand-Archive -Path <zip_file_path>
```


