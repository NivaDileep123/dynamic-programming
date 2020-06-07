#lcs memoization
st1=input("Enter the first string:")
l1=list(st1)
n=len(l1)
st2=input("Enter the second string:")
l2=list(st2)
m=len(l2)
print(n,m)
t=[[0 for i in range(m+1)]for j in range(n+1)]
def lcs(l1,l2,n,m):
    
    #base condition
    if (n==0 or m==0):
        return 0
    if (t[n][m]!=0):
        return t[n][m]
    #choice diagram
    if (l1[n-1]==l2[m-1]):
        t[n][m]=1+lcs(l1,l2,n-1,m-1)
        return t[n][m]
    else:
        t[n][m]=max(lcs(l1,l2,n-1,m),lcs(l1,l2,n,m-1))
        return t[n][m]
print("lcs is:",lcs(l1,l2,n,m))
print(t)
