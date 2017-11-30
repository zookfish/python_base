


bri = set(['int','long','double','float','enum'])

# set不支持切割
# print(bri[:])
# print(bri[::2])
print('int' in bri)
bric = bri.copy()
bric.add('class')
print(bric.issuperset(bri))

bri.remove('long')
print(bri & bric)
