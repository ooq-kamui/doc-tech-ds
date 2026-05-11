
# vite & cloud9


## cloud9 で vite の `npm run dev` を確認する方法

setting

`vite.config.ts`

```
export default defineConfig({

  // :    plugins: [react()], などの記述

  server: {
    allowedHosts: ['xxxxxxxxxxxxxxxx.vfs.cloud9.ap-northeast-1.amazonaws.com'],
  },
})
```

起動

```
npm run dev -- --port 8080
```

local の pc の browser で  
xxxxxxxxxxxxxxxx.vfs.cloud9.ap-northeast-1.amazonaws.com  
にアクセスすれば, 表示されるはず


