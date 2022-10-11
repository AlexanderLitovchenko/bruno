d = {'name1':'id1','name2':'id2','name3':'id3'}
n = {}

for key, value in d.items():
     n[value] = key
     d = n
print(d)

