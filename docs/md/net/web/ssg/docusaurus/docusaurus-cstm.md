
# customize


## search ( 検索 ) の設置

`@easyops-cn/docusaurus-search-local` を使用する

```
npm install --save @easyops-cn/docusaurus-search-local
```

`-g` で global に入れてもダメのよう


docusaurus.config.js を編集

下記を追記

```
const config = {
  // :
  themes: [
    [
      require.resolve("@easyops-cn/docusaurus-search-local"),
      /** @type {import("@easyops-cn/docusaurus-search-local").PluginOptions} */
      ({
        // ... Your options.
        indexDocs:  true,
        indexBlog:  false,
        indexPages: false,
        docsRouteBasePath:"/",
        // `hashed` is recommended as long-term-cache of index file is possible.
        hashed: true,
        // For Docs using Chinese, The `language` is recommended to set to:
        language: ["ja", "en"],
      }),
    ],
  ],
```

header に search result page を追加

docusaurus.config.js を編集

```
  themeConfig:
      // :
      navbar: {
        // :
        items: [
          {to: '/search', label: 'search', position: 'left'},
```

この検索は test run  ( `npm start` ) では作動しないので注意


## `Edit this page` を外す

docusaurus.config.js を編集

下記の `editUrl` を削除

```
  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          routeBasePath: '',
          sidebarPath: './sidebars.js',
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          // editUrl:
          //   'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
```


## sidebar を閉じる

docusaurus.config.js を編集

docs の場合

```
  // :
  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      // :
      docs: {
        sidebar: {
          hideable: true,
        },
      },
      // :
```



