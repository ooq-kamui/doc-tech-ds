

a = {}
a['a'] = 'a'

# a['b'] = 'b1'


b = a['b'] if 'b' in a else 'b2'

print(b)


