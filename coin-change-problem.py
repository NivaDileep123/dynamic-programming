#coin change problem
totalrupee=int(input("Enter total rupee to change:"))
coins=list(map(int, input("Enter the coins:").split()))
n=len(coins)
t=[[0 for j in range(totalrupee + 1)]for i in range(n+1)]
for i in range(n+1):
    for j in range(totalrupee+1):
        if(i==0)or(j==0):
            if(i==0):
                t[i][j]=0
            if(j==0):
                t[i][j]=1
        else:
            if(coins[i-1]<=totalrupee):
                t[i][j]=t[i][j-coins[i-1]]+t[i-1][j]
            else:
                t[i][j]=t[i-1][j]
print("No.of ways=",t[i][j])
