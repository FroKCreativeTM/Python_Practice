def testFunc(dic) : 
	for k in dic.keys() : 
		print(k)
	for v in dic.values() : 
		print(v)

dic = {'name' : 'frok',
	   'phone' : '010-5057-2990',
	   'birth' : '1995-12-04'}

testFunc(dic)
dic.clear()