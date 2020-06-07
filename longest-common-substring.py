#longest common substring
s1=input("Enter the first string:")
l1=list(s1)
n=len(l1)
s2=input("Enter the second string:")
l2=list(s2)
m=len(l2)
t=[[0 for j in range(m+1)]for i in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        if (l1[i-1]==l2[j-1]):
            t[i][j]=1+t[i-1][j-1]
        else:
            t[i][j]=0
print(t)
large=0
for i in range(1,n+1):
    for j in range(1,m+1):
        if(t[i][j]>large):
            large=t[i][j]
print("longest common substring is:",large)
            
