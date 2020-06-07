#min no.of deletion to convert string to palindrome
st1=input("Enter a string:")
l1=list(st1)
l2=l1[::-1]
n=len(l1)
m=n
t=[[0 for j in range(m+1)]for j in range(n+1)]
for i in range(n):
    for j in range(m):
        if (l1[i-1]==l2[j-1]):
            t[i][j]=1+t[i-1][j-1]
        else:
            t[i][j]=max(t[i-1][j],t[i][j-1])
print("lps is:",t[i][j])
print("min no.of deletions to convert string to palindrome:",n-t[i][j]) 
