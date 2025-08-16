
str   = 'abcdefg'
ptn   = 'de'
-- ptn   = 'h'
srch_s_idx = 0

match, e_idx, match = string.match(str, ptn, srch_s_idx)
print(s_idx, e_idx, match)


