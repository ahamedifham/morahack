import sys
lines=[]
firstPic=[]
secondPic=[]
for line in sys.stdin:
    lines.append(line)
numbers=lines[0].split()
l=int(numbers[0])
h=int(numbers[1])
#print l
#print h
for i in range(1,h+1):
    firstPic.append(lines[i].strip('\n'))
for j in range(h+1,2*h+1):
    secondPic.append(lines[j].strip('\n'))

ss=set(firstPic)
fs=set(secondPic)
inter= ss.intersection(fs)
unio = ss.union(fs)
diff= unio - inter
#print (len(diff))
if (len(diff)==0):
    print 'X'
else:
