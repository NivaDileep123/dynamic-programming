#lcs recursive
def lcs(l1,l2,n,m):
    #base condition
    if (n==0 or m==0):
        return 0
    #choice diagram
    if (l1[n-1]==l2[m-1]):
        return (1+ lcs(l1,l2,n-1,m-1))
    else:
        return max(lcs(l1,l2,n,m-1),lcs(l1,l2,n-1,m))
st1=input("Enter the first string:")
l1=list(st1)
st2=input("Enter the second string:")
l2=list(st2)
n=len(l1)
m=len(l2)
print("longest common subsequence is:",lcs(l1,l2,n,m))                
        
