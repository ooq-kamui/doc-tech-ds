
# sed option


## regex

```
-e      正規表現
-E  拡張正規表現
-r  拡張正規表現
```

拡張正規表現 を使うのが無難


## 実行結果 を 入力ファイル に 上書き保存 する

```
sed -i '' -e "s/srch/rpl/g" file_name.txt
```


