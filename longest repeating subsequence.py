#longest repeating subsequence
#lcs tabulation
st1=input("Enter the first string:")
l1=list(st1)
n=len(l1)
l2=l1
print(l2)
m=len(l2)
t=[[0 for j in range(m+1)]for j in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        if ((l1[i-1]==l2[j-1]) and (i!=j)):
            t[i][j]=1+t[i-1][j-1]
        else:
            t[i][j]=max(t[i-1][j],t[i][j-1])
print(t)
print("lcs is",t[i][j])
