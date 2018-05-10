j=int(input())
a=[]
t=""
s=""
if(1 <= j <=100000):
	for i in range(j):
		a.append(int(input()))
a.sort()
if sum(a)>0:
	for i in range(j):
		t=t+str(a[i])
	s=t[::-1]
else:
	s="0"
print(s)