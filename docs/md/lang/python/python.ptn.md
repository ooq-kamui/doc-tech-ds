
# ptn


## re

```
import re

TIMESTAMP_D_PTN = r"\d{4}-\d{2}-\d{2}"
ptn_d = re.compile(TIMESTAMP_D_PTN)

str_d = "2024-11-02"
str_s = "2024-11-02 01:02:03"

if ptn_d.fullmatch(str_d):
    print("d: match")
else:
    print("d: not")

if ptn_d.fullmatch(str_s):
    print("d: match")
else:
    print("d: not")
```

reslt

```
d: match
d: not
```

`ptn.fullmatch(str)` だと 自動で `ptn` が `^ptn$` になるイメージ



