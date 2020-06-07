#longest palindrome sunsequence
st1=input("Enter the string:")
l1=list(st1)
n=len(l1)
l2=l1[::-1] #reversing l1
m=n
t=[[0 for j in range(m+1)]for j in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        if (l1[i-1]==l2[j-1]):
            t[i][j]=1+t[i-1][j-1]
        else:
            t[i][j]=max(t[i-1][j],t[i][j-1])
print("lps is",t[i][j])
