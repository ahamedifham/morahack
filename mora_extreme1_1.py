import sys
def replaceSS(temp1, finalOutPut):
    temp2= temp1
    finalOutPut=finalOutPut
    if 'ss' in temp2:
        l= temp2.find('ss')
        temp2= temp2.replace('ss','h',1)
        finalOutPut = finalOutPut + temp2[0:l+1]
        temp3=temp2[l+1:]
        return replaceSS(temp3, finalOutPut)
    else:
        finalOutPut= finalOutPut +temp2
        #print finalOutPut
        return finalOutPut

def replaceHH(temp1, finalOutPut):
    temp2= temp1
    finalOutPut=finalOutPut
    if 'hh' in temp2:
        l= temp2.find('hh')
        temp2= temp2.replace('hh','s',1)
        finalOutPut = finalOutPut + temp2[0:l+1]
        temp3=temp2[l+1:]
        return replaceHH(temp3, finalOutPut)
    else:
        finalOutPut= finalOutPut +temp2
        return finalOutPut

#str1=raw_input()
#str1 = "5 ssssshsssh hhhhhs sshshshssh hshsh shhssshsss"
list1=[]
for line in sys.stdin:
    list1.append(line)
#list1=str1.split()
#no_of_tests=int(list1[0])
no_of_tests = len(list1)-1

finalmemo=''
for i in range(1,no_of_tests+1):
    tempString=list1[i]
    checkForSS=False
    checkForHH= False

    if 'ss' in tempString:
        checkForSS=True
    if 'hh' in tempString:
        checkForHH= True
    while(checkForHH==True or checkForSS==True):
        if checkForSS==True:
            tempString =replaceSS(tempString, '')
            #print tempString
            checkForSS=False
            if 'hh' in tempString:
                checkForHH= True
            #print tempString
        if checkForHH==True:
            tempString = replaceHH(tempString,'')
            #print tempString
            checkForHH=False
            if 'ss' in tempString:
                checkForSS= True

    if(checkForHH==False and checkForSS==False):
        noOfH= tempString.count('h')
        noOfS= tempString.count('s')
        #print str(noOfH)

        finalmemo=finalmemo + str(noOfH) + ' ' + str(noOfS) + '\n'




print finalmemo
