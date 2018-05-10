j=int(input())
i=int(input())
k=0
count=0
for t in range(j,i+1):
	for inn in range(2,t+1):
		if(t%inn==0):
			k=k+1
	if(k==1):
		count=count+1
		k=0
	else:
		k=0
print(count)
