r=3
n=4
totalRecursions = (r+1)**n
memo={}
for i in range(1,n+1):
    memo[i]=0
print memo
#for i in range(0, totalRecursions):
for i in range(1, n+1):
    for j in range(i,n+1):
        for k in range(0, r+1):
            for l in range(k,r+1):
                memo[i]=k
                memo[j]=l
                print memo
                if(j!=n):
                    temp1=memo[j]
                    temp2=memo[j+1]
                    #print temp1-temp2
                else:
                    print memo[j]-memo[j-1]
