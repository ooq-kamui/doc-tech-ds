
# hugo


## todo

### draft をみる方法 ある?



---

## test

```
hugo server
```


---

## learn site
```

```


## init

```
hugo new site hugo_dir
```


## theme dl

```
cd hugo_dir_root
cd themes
git clone https://github.com/MunifTanjim/minimo.git
```


## theme sample copy

```
cd hugo_dir_root
cp -r themes/minimo/exampleSite/ .
```


## side menu category
data/config/widgets.toml
```
[taxonomy_cloud]
taxonomy = "categories"
```

## category artcl lst num
config.toml
```
Paginate = 15
```


## post article new
```
hugo new category/file_name.md
```



## q&a

- md header の url 入れないといけない?

  - ないとどうなる?
    - url は ファイル名になる
  - 重複する場合はどうなる?
    - どれか 1つしか表示されない



