j=int(input())
a=[]
t=""
if(1 <= j <=100000):
	for i in range(j):
		a.append(int(input()))
a.sort()
for i in range(j):
	t=t+str(a[i])
print(t[::-1])