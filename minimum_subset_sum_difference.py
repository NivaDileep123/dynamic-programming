#minimum subset sum difference
arr=list(map(int,input("Enter the array:").split()))
n=len(arr)
sum=sum(arr)
#subsetsum
t=[[False for j in range(sum+1)]for i in range(n+1)]
for i in range(n+1):
    for j in range(sum+1):
        if (i==0)or (j==0):
            if (i==0):
                t[i][j]=False
            if (j==0):
                t[i][j]=True
        else:
            if (arr[i-1]<=j):
                t[i][j]=(t[i-1][j-arr[i-1]] or t[i-1][j])
            elif (arr[i-1]>j):
                t[i][j]=t[i-1][j]
print(t)

s1=[]
j=0
for j in range((sum//2)+1):
    if (t[i][j]==True):
        s1.append(j)
print(s1)
mn=sum
for m in range(len(s1)):
    mn=min(mn, sum-(2*s1[m]))
print(mn)

        
    


         
