import sys
def checkForTwo(value,arrayOfNumbers):
    flag3=False
    for i in range(len(arrayOfNumbers), 1, -1):
        if(flag3 == True):
            break
        else:
            for j in range(1,len(arrayOfNumbers)):
                tempValue = arrayOfNumbers[i] + arrayOfNumbers[j]
                if(tempValue==value):
                    flag3=True
                    break
                elif(tempValue>value):
                    break
                else:
                    continue
    if(flag3==True):
        return 2
    else:
        return 3

def checkForThree(value, arrayofNumbers):
    flag4=False
    for i in range(len(arrayofNumbers),1,-1):
        if (flag4 == True):
            break
        else:
            for j in range(len(arrayofNumbers),1,-1):
                if (flag4==True):
                    break
                else:
                    for k in range(1,len(arrayofNumbers)):
                        tempValue =  arrayofNumbers[i] + arrayofNumbers[j] + arrayofNumbers[k]
                        if(tempValue==value):
                            flag4=True
                        elif(tempValue>value):
                            break
                        else:
                            continue

    if (flag4==True):
        return 3
    else:
        return 4


#str1 = "3 75 3 883"
#listOfNumbers = str1.split()
listOfNumbers=[]
for line in sys.stdin:
    listOfNumbers.append(line)
noOfTestCases= int(listOfNumbers[0])
finalOutPut = {}
for i in range(1, len(listOfNumbers)):
    test1 = int(listOfNumbers[i])
    flag1=True
    upperlimit=test1/2

    while(flag1):
        if (upperlimit**2>test1):
            #print 'upperlimit **2 is ' , upperlimit**2
            upperlimit=upperlimit//2
            #print upperlimit
        else:
            flag1=False
    upperlimit=upperlimit*2
    #print upperlimit
    flag2=True
    while(flag2):
        if(upperlimit**2>test1):
            upperlimit= upperlimit-1
        else:
            flag2=False
    #print upperlimit
    memo={}
    for i in range(1,upperlimit+1):
        memo[i]= i**2
    if(test1 in memo.values()):
        finalOutPut[test1]=1
    else:
        checkInput = checkForTwo(test1,memo)
        if (checkInput==2):
            finalOutPut[test1]=2
        else:
            checkInput= checkForThree(test1, memo)
            if(checkInput==3):
                finalOutPut[test1]=3
            else:
                finalOutPut[test1]=3
for i in range(1, len(listOfNumbers)):
    print finalOutPut[int(listOfNumbers[i])]
