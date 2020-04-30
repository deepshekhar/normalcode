name=input("enter a file name")                 #program to read a file and arrange the words in a list in alphabetical order.There
fname=open(name)                                        #is no repetation of words and each word is taken once
di=dict()

for line in fname:
    words=line.split()
    for word in words:
        di[word]=di.get(word,0) + 1
lst=list()
for key,value in di.items():
    lst.append(key)
    
lst.sort()
print(lst)
