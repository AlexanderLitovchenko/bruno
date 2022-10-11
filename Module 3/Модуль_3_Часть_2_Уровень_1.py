l = [1,4,1,5,'hello',6,'a',4,2,3,9,9,6,'hello','a',5,'hello']
newlist = []
for i in l:
	if i not in newlist:
		newlist.append(i)
print(newlist)


#or  
#print(list(set(l)))

