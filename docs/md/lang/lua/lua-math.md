
# lua math


## 小数の切り捨て表示

```
> val = 123.456
> print(string.format("%7.2f", val))
 123.46

-- 7 は . も入れた全体の文字数
-- 小数切り捨てはおおむね四捨五入のようだが厳密でないときもある
```


## ランダム値を得る

math.randomseed() をしても最初の math.random() はランダム値にならない  
仕様のようなので1回ダミーで math.random() を実行する  
2回目以降はランダム値が得られます

```
math.randomseed(os.time())
math.random(1,  2) -- dumy, 1回目はランダム値が得られないため
math.random(1, 10) -- 1 - 10 のいずれかの整数を得る
```


