#print shortest common supersequence
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
            t[i][j]=max(t[i-1][j],t[i][j-1])
print(t)
s=''
i=n
j=m
while (i>0 and j>0):
    if (l1[i-1]==l2[j-1]):
        s=s+str(l1[i-1])
        i=i-1
        j=j-1
    else:
        if(t[i-1][j]>t[i][j-1]):
            s=s+str(l1[i-1])
            i=i-1
        else:
            s=s+str(l2[j-1])
            j=j-1
while(i>0):
    s=s+str(l1[i-1])
    i=i-1
while(j>0):
    s=s+str(l2[j-1])
    j=j-1
sr=''
for i in s: 
    sr = i + sr
print(sr)
