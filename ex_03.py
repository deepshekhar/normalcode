name=input("Enter a file name")        #code that reads a file and reads all the numbers presents in it and gives the total
fname=open(name)
gname=fname.read()
total=0.0
y=list()
import re
y=re.findall('[0-9]+',gname)

for i in range(0,len(y)):
    total=total+ float(y[i])
print(total)
