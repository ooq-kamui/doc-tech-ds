
# sys args


## コマンドラインからの引数

```
import sys

sys.argv
```

ex

```
_ cat tst.args.py
import sys

for idx, val in enumerate(sys.argv):

    print(idx, val)


_ python tst.args.py a b
0 tst.args.py
1 a
2 b
_
```



