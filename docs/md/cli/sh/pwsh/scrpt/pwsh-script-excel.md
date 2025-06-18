
# excel


## import

ImportExcel を使用

### install

```
Install-Module -Name ImportExcel
```

### 使用方法

ex

```
$excel = Import-Excel $excel_file_path -worksheetName $excel_sheet_name -NoHeader -EndColumn $col_num_max
```

option

```
-worksheetName  <sheet_name>
-NoHeader                      1 行目を header 行として読み込まない, default は 1 行目 を header として読み込む
-EndColumn      <col_num_max>

```


