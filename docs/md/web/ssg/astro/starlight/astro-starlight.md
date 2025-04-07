
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


## site title

astro.config.mjs

```
export default defineConfig({
  integrations: [
    starlight({
      title: 'vmw-mgn',
      // :
```


## frontmatter

### require

```
---
title: page 001
---

```


## side menu

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


