#minimum no.of insertion and deletion to convert a to b
st1=input("Enter the first string:")
l1=list(st1)
n=len(l1)
st2=input("Enter the second string:")
l2=list(st2)
m=len(l2)
t=[[0 for j in range(m+1)]for j in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        if (l1[i-1]==l2[j-1]):
            t[i][j]=1+t[i-1][j-1]
        else:
            t[i][j]=max(t[i-1][j],t[i][j-1])
print("lcs is",t[i][j])
print("no.of deletions is:",n-t[i][j])
print("no.of insertions is:",m-t[i][j])
