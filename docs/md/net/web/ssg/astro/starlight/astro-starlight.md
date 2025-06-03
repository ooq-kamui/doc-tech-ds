
# starlight


## ref

```
https://starlight.astro.build/getting-started/
```


## app cre

```
npm create astro@latest -- --template starlight
```


## local dev run

```
npm run dev
```


## md doc dir

```
src/content/docs/
```


## もとの top page を消す

- もとの index.mdx を cp で buckup
- index.mdx の中身を消す


## site title

astro.config.mjs

```
export default defineConfig({
  integrations: [
    starlight({
      title: 'vmw-mgn',
      // :
```

## site logo

astro.config.mjs

```
export default defineConfig({
  integrations: [
    starlight({
      // :
      logo: {
        src: './src/assets/starlight.svg',
      },
      // :
```


## frontmatter

### require

```
---
title: page 001
---

```


## side nav ( menu )

### cnf

astro.config.mjs

```
export default defineConfig({
  integrations: [
    starlight({
      // :
      sidebar: [
        {
          label: 'tst',
          autogenerate: { directory: 'tst' },
        },
        // :
```

### dir view string

saide navi での dir の表示名を dir name とは別に変えたい場合

astro.config.mjs

```
export default defineConfig({
  integrations: [
    starlight({
      // :
      sidebar: [
        {
          label: 'Guides',
          autogenerate: { directory: 'guides' }, // guidesディレクトリのリンクグループを自動生成します。
        },
        // :
```

### order

#### file

```
---
sidebar:
  order: 1
---
```

#### dir

```
sidebar の label 定義順 で 指定するのが無難
( いまのところ )
```


### close

```
できない かも ?

wip:
```


