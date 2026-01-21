
# wez term


## cnf file

### win

```
$HOME/.config/wezterm/wezterm.lua
```

### mac

```
~/.config/wezterm/wezterm.lua
```


## default sh

### pwsh

```
default_prog = {'pwsh'}
```

### wsl

```
default_prog = {'wsl'}
```

#### wsl で 複数の distro の場合

```
config.wsl_domains = {
  {
    name = 'wsl:alm-10-my-01',
    distribution = 'alm-10-my-01', -- wsl -l -v で表示される distro name
    default_cwd = '~',
  },
}

config.default_domain = 'wsl:alm-10-my-01' -- 上記 wsl_domains の name
```


## debug overlay

- ctrl + shift + l で debug overlay mode になる
- log を見れる
- lua 実行できる


## log

lua 内に 下記 fnc で log 出力できる

```
wezterm.log_info()
```

- ctrl + shift + l で debug overlay mode にすると,  
  そこまでに `wezterm.log_info()` した log を見れる


## lua の実行

- ctrl + shift + l で debug overlay mode にすると,  
  最下部に プロンプト `>` が表示される  
- ここで interactive で lua の実行ができる


## 現在の color scheme を確認

- ctrl + shift + l で debug overlay mode にする

```
window:get_config_overrides().color_scheme
```


## color

### ansi-color-16

```
Black
Maroon
Green
Olive
Navy
Purple
Teal
Silver
Grey
Red
Lime
Yellow
Blue
Fuchsia
Aqua
White
```


## key-bind

### output lua file

```
wezterm show-keys --lua > keybinds.lua
```


## iem

- iem とは windows iem のことだけを指しているのではない
  - mac でも 設定する


## ref

https://wezterm.org/

https://zenn.dev/mozumasu/articles/mozumasu-wezterm-customization

https://gentoo.hatenablog.com/entry/2024/10/04/161346

https://medium.com/@yusuke_h/%E3%82%BF%E3%83%BC%E3%83%9F%E3%83%8A%E3%83%AB%E3%81%8C%E3%83%80%E3%82%B5%E3%81%84%E3%81%A8%E3%83%A2%E3%83%86%E3%81%AA%E3%81%84-wezterm%E7%B4%B9%E4%BB%8B%E7%B7%A8-11306091722a

https://dev.classmethod.jp/articles/wezterm-get-started/

https://qiita.com/sonarAIT/items/0571c869e5f9ab3be817

https://zenn.dev/yutakatay/articles/wezterm-intro


