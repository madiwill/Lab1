z=input("Enter file")
victors=open(z)
necessary=[]
for x in victors:
	c=x.split()
	necessary.append(c)
dictionary={}
for x in necessary:
	for d in x:
		if d not in dictionary:
			dictionary[d]=1
		else:
			dictionary[d]+=1
real=[]
for x,v in dictionary.items():
	real.append((v,x))
sure=sorted(real,reverse=True)
z=sure[0:15]
for x in z:
	print(x[1],x[0])