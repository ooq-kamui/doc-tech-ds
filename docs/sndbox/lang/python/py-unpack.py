


a = {
  'key01' : 1,
  'key02' : 2,
}


print(a)
print(*a)
# print(**a)


def fnc01(prm01, prm02, prma):

  print(prm01, prm02, prma)


p = {
  'prma'  : 'a',
  'prm01' : 1,
  'prm02' : 2,
}

fnc01(*p)
fnc01(**p)


