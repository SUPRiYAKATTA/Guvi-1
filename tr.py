import subprocess
 

i=input()
txt=""
s=""
for t in i.split():
	s=s+t
tx =s+".py"
txt=tx
print(tx)
subprocess.run(['clip.exe'], input=txt.encode('utf-16'), check=True)
