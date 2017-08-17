import sys
#str1 = "5 1994"
str2=sys.stdin
str1=str2.read()
listOfNumbers = str1.split()
k=int(listOfNumbers[0])
b=int(listOfNumbers[1])


finalmemo={}
for n in range(1,b):
    if (n<3):
        finalmemo[n]=n
        #print finalmemo
    elif(n<k):
        finalmemo[n]=n
        #print finalmemo
    else:
        if not n in finalmemo:
            remainder = n%k
            if(remainder==0):
                functionValue = n/k
                if not n/k in finalmemo:
                    finalmemo[n]= functionValue
                else:
                    finalmemo[n] = finalmemo[n/k]
            else:
                valueWithoutRemainder = n-remainder
                functionValue=valueWithoutRemainder/k
                if not valueWithoutRemainder/k in finalmemo:
                    finalmemo[n]=functionValue + remainder
                else:
                    finalmemo[n]=finalmemo[valueWithoutRemainder/k]+remainder
        #else:
        #    tempValue = finalmemo[n]
        #    remainder = n%k
        #    if(remainder == 0):
        #        functionValue = n/k
        #        tempValue2 = functionValue
        #    else:
        #        valueWithoutRemainder = n-remainder
        #        functionValue = valueWithoutRemainder/k
        #        tempValue2 = functionValue + remainder
        #    if (tempValue>tempValue2):
        #        finalmemo[n]=tempValue
        #    else:
        #        finalmemo[n]=tempValue2
#print finalmemo
tempMaxKey=1
for i in range(1, len(finalmemo)):
    if (finalmemo[i]>finalmemo[tempMaxKey]):
        tempMaxKey= i
    elif (finalmemo[i]==finalmemo[tempMaxKey]):
        continue
#print finalmemo

print tempMaxKey
