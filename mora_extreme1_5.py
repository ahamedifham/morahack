import sys
import operator
#a=2
#b=2
lines=[]
listofWords=[]
listOfExcuses=[]
for line in sys.stdin:
    lines.append(line)
numbers=lines[0].split()
a=int(numbers[0])
b=int(numbers[1])

for i in range(1,a+1):
    listofWords.append(lines[i].strip('\n'))
for j in range(a+1,b+a+1):
    listOfExcuses.append(lines[j].strip('\n'))
finalcount=[]
for k in range(0,len(listOfExcuses)):
    tempCount1=0
    for l in range(0,len(listofWords)):
        #count = listOfExcuses[k].count(listofWords[l])
        #print count
        #print listOfExcuses[k].split()
        #print listofWords[l] in listOfExcuses[k].split()
        tempCount2 = listOfExcuses[k].split().count(listofWords[l])
        tempCount1= tempCount1 + tempCount2
    finalcount.append(tempCount1)

maxKey=0
for m in range(0, len(listOfExcuses)):
    if finalcount[m]>maxKey:
        maxKey=m
    else:
        continue

print listOfExcuses[maxKey]
