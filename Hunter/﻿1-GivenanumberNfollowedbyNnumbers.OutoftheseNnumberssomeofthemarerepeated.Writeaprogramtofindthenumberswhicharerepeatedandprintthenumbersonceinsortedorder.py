size=int(input())
a=[]
for i in range(size):
	a.append(int(input()))
for i in set(a):
	a.remove(i)
print(sorted(a))