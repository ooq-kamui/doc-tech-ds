
# docusaurus


## 既存の markdown file 群 を docusaurus の site にする 方法

### directory create

```
npx create-docusaurus@latest doc01 classic
```

directory `doc01` が作成される

内容は下記のようなもの

ex

```
_ cd doc01
_ ll
total 1208
drwxr-xr-x   19    608B 2024-07-21 03:22 .docusaurus
-rw-r--r--    1    233B 2024-07-18 04:16 .gitignore
-rw-r--r--    1    768B 2024-07-18 04:16 README.md
-rw-r--r--    1     89B 2024-07-18 04:16 babel.config.js
drwxr-xr-x   22    704B 2024-07-21 03:37 build
drwxr-xr-x   15    480B 2024-07-20 09:07 docs
-rw-r--r--    1    4.7K 2024-07-21 06:05 docusaurus.config.js
drwxr-xr-x  753     24K 2024-07-21 02:41 node_modules
-rw-r--r--    1    570K 2024-07-21 02:41 package-lock.json
-rw-r--r--    1    1.1K 2024-07-21 02:41 package.json
-rw-r--r--    1    779B 2024-07-18 04:16 sidebars.js
drwxr-xr-x    5    160B 2024-07-18 04:16 src
drwxr-xr-x    4    128B 2024-07-18 04:16 static
```

### markdown file 群を 設置する

directory `docs` の中に markdown file 群 を入れる


docusaurus.config.js の修正

下記の `routeBasePath: '',` の行を追加

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
          editUrl:
            'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
        },
```

とりあえず 仮 の top page を設置

`docs/index.md`

とりあえず 仮 なので, 内容は下記

```
# home

```


### 不要なものを削除

#### もとからある top page を削除

```
rm src/pages/index.js
```

#### header から不要なものを削除

docusaurus.config.js を編集

下記の `navbar > items` 内はすべて削除

```
      navbar: {
        title: 'doc tech',
        logo: {
          alt: 'My Site Logo',
          src: 'img/logo.svg',
        },
        items: [
          // {
          //   type: 'docSidebar',
          //   sidebarId: 'tutorialSidebar',
          //   position: 'left',
          //   label: 'Tutorial',
          // },
          // {to: '/blog', label: 'Blog', position: 'left'},
          // :
```

#### footer から不要なものを削除

docusaurus.config.js を編集

下記の `footer > links` 内はすべて削除

```
      footer: {
        style: 'dark',
        links: [
          // {
          //   title: 'Docs',
          //   items: [
          //     {
          //   :
```

#### blog を削除

directory `blog` を削除


### 起動

#### test 起動

このあたりで 1回 試してみる
( 慣れないうちは, 上記の 1 step ずつ試すのが無難 )

```
npm start
```

自動で `localhost:3000` が起動する

err だった場合は 適宜 見直す


#### build して 本起動

build

```
npm run build
```

起動

```
npm run docusaurus serve
```


### search ( 検索 ) の設置

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


### site title を変える

docusaurus.config.js を編集

下記の `My Site` の部分を変える

```
const config = {
  title: 'My Site',

  // :

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      // Replace with your project's social card
      image: 'img/docusaurus-social-card.jpg',
      navbar: {
        title: 'My Site',
        // :
```

### logo img ( 左上 ) を変える

docusaurus.config.js を編集

下記の `navbar > logo > src` を変える

```
  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      // Replace with your project's social card
      image: 'img/docusaurus-social-card.jpg',
      navbar: {
        title: 'My Site',
        logo: {
          alt: 'My Site Logo',
          src: 'img/logo.svg',
        },
```


### `Edit this page` を外す

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


### sidebar を閉じる

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



## 謎の link 不正エラーが出た場合

とりあえず,
markdown file すべてに対して 空行 1行追加

で, 再 build で直る

詳細不明



## ref

https://zenn.dev/koushikagawa/scraps/6f38fbc8a2b3ee

https://zenn.dev/koushikagawa/articles/74392990d399ed

https://note.com/scg_tech/n/n2a93df1a69e2

http://ducaneko.starfree.jp/start-on-docusaurus/



