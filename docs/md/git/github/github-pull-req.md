
# git  -  pull-req


## pull req とは

- remote 上で branch01 から branch02 に merge する, その提案
- git の command 操作としては, やっているのは merge なのだが,  
  github では これを pull req と名付けている


## github の pull req でできる merge の種類

- 3 way ( no ff )
- squash
- rebase


## notice

- githug の pull req で `first forward` はできません


## squash merge

### q

remote で, pull req から squash merge された場合,  
local で その branch を 継続して 利用できるか ?

### a

- できない ( たぶん )
- 仮にできたとしても, commit history の意味がわからなくなるので, 使用しないのが無難


## ref

- https://qiita.com/kuuuuumiiiii/items/42d2d9ed11e3b29c22cf
- https://zenn.dev/gachigachi/articles/dcd833c56bd0ed



