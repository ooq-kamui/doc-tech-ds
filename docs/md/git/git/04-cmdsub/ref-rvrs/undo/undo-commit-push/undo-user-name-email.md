
# push 済みコミットの author/email を rebase で修正する方法

## 手順

### 1. 修正対象の範囲を決める

```bash
# 直近 N コミットを対象にする場合
git rebase -i HEAD~N
```

または, 特定のコミット以降すべてを対象にしたいなら:

```bash
git rebase -i <修正したい最古のコミットの1つ前のハッシュ>
```

### 2. エディタで対象コミットを `edit` に変更

開いたエディタで, 修正したいコミットの `pick` を `edit` に書き換えて保存・終了する.

```
edit abc1234 some commit message
pick def5678 another commit
```

### 3. author 情報を書き換える

rebase が止まったら以下を実行:

```bash
git commit --amend --author="New Name <new@email.com>" --no-edit
```

`edit` にしたコミットが複数ある場合は, 都度これを実行してから:

```bash
git rebase --continue
```

を繰り返す.

### 4. force push する

```bash
git push --force-with-lease
```

`--force-with-lease` は, 他の人が同じブランチに push していた場合に上書きを防いでくれるので, `--force` より安全.

---

## 全コミットを一括で書き換えたい場合

対象が多いなら `rebase -i` + `exec` で一発で回せる:

```bash
git rebase -i HEAD~N --exec 'git commit --amend --author="New Name <new@email.com>" --no-edit'
```

この場合はエディタで何も変更せずそのまま保存すれば, すべてのコミットに対して `--exec` のコマンドが走る.

---

## 注意点

- force push はリモートの履歴を書き換えるため, 共同作業者がいる場合は事前に周知が必要
- `--force-with-lease` でも, 他の人が既に `fetch` 済みのコミットを壊すことに変わりはない
- `committer` 情報も揃えたい場合は, rebase 前に `user.name` / `user.email` を設定しておく:

```bash
git config user.name "New Name"
git config user.email "new@email.com"
```

こうすると rebase 時に committer が自動的に現在の設定値で上書きされる.


