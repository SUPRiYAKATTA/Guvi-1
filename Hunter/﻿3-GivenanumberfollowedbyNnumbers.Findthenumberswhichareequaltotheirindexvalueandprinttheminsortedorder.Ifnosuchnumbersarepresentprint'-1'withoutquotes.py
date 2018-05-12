size=int(input())
if 0<size<100000:
		a=[]
		j=0
		b=[]
		for i in range(size):
			a.append(int(input()))
		for i in a:
			if j==i:
				b.append(j)
				j=j+1
			else:
				j=j+1
		if len(b)<1:
			print(-1)
		else:
			print(sorted(b))
