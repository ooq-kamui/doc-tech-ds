
str   = 'abc defg'

-- ptn   = 'de'
ptn   = '%s'
-- ptn   = 'h'

srch_s_idx = 0

s_idx, e_idx = string.find(str, ptn, srch_s_idx)
print(s_idx, e_idx)


