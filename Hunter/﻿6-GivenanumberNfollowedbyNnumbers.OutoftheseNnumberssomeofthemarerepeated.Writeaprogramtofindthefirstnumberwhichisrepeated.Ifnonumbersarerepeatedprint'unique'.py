size=int(input())
if 0<size<100000:
	a=[]
	b=[]
	for i in range(size):
		a.append(int(input()))
	for i in set(a):
		a.remove(i)
	if len(a)<1:
		print("Unique")
	else:
		print(a[0])