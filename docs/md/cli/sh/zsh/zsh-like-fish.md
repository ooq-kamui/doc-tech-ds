
# zsh like fish


## zsh-autosuggestions

### install

```
git clone https://github.com/zsh-users/zsh-autosuggestions ~/.zsh/zsh-autosuggestions
```

### setting

```
source ~/.zsh/zsh-autosuggestions/zsh-autosuggestions.zsh
```


## zsh-syntax-highlighting

### install

```
git clone https://github.com/zsh-users/zsh-syntax-highlighting ~/.zsh/zsh-syntax-highlighting
```

### setting

```
source ~/.zsh/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
```


## compinit + zstyle menu select ( autocomplete )

### setting

```
autoload -Uz compinit
compinit
zstyle ':completion:*' menu select
```


