
# pnpm from npm


## 移行方法

- 前提
  - pnpm は install 済

prj dir で

package-lock.json から pnpm-lock.yaml を作る

```
pnpm import
```

```
rm -rf node_modules package-lock.json
```

```
pnpm install
```

```
pnpm build
```

- notice
  - build で, 依存関係の err が出た場合
  - `.npmrc` に `node-linker=hoisted` を書くと  
    npm と同じ配置になり, たいていは解決する


