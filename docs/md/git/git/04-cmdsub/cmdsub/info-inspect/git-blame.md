
# git blame

- ファイルの各行を  
  誰が, いつ, どのコミットで最後に変更したか  
  を表示するコマンド


## 基本的な使い方

```bash
git blame path/to/file.txt
```

出力例:

```
a1b2c3d4 (Alice  2025-03-10 14:22:01 +0900  1) function hello() {
e5f6g7h8 (Bob    2025-04-05 09:11:32 +0900  2)   return "world";
a1b2c3d4 (Alice  2025-03-10 14:22:01 +0900  3) }
```


## 主な用途

- バグの原因となった変更を特定する
- ある行がなぜそう書かれたか, コミットメッセージから意図を辿る
- コードの担当者を把握する


## よく使うオプション

```bash
# 特定の行範囲だけ見る (10行目〜20行目)
git blame -L 10,20 file.txt

# 空白の変更を無視する
git blame -w file.txt

# コード移動元も追跡する (ファイル内の移動)
git blame -M file.txt

# 他ファイルからのコピーも追跡する
git blame -C file.txt
```


