arr=list(map(int, input("Enter the array:").split()))
n=len(arr)
sum=int(input("Enter the sum:"))
t=[[0 for j in range(sum+1)]for i in range(n+1)]
for i in range(n+1):
    for j in range(sum+1):
        if (i==0) or (j==0):
            if (i==0):
                t[i][j]=0
            if (j==0):
                t[i][j]=1
        else:
            if (arr[i-1]<=j):
                t[i][j]=(t[i-1][j-arr[i-1]])+(t[i-1][j])
            elif (arr[i-1]>j):
                t[i][j]=t[i-1][j]

print(t)
print("count is ",t[i][j])
