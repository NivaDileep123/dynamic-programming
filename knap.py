wt=list(map(int, input("weights:").split()))
val=list(map(int, input("values:").split()))
n=len(wt)
w=int(input("Enter sack's capacity:"))

t=[[-1 for i in range(w+1)] for j in range(n+1)]

def knapsack(wt, val, w, n):
    if (n==0) or (w==0):
        return 0
    if t[n][w]!=-1:
        return t[n][w]

    if wt[n-1]<=w:
        t[n][w]=max(val[n-1]+ knapsack(wt,val,w-wt[n-1],n-1), knapsack(wt, val, w, n-1))
        return t[n][w]
    elif wt[n-1]>w:
        t[n][w]= knapsack(wt, val, w, n-1)
        return t[n][w]
print("maximum value:",knapsack(wt, val, w, n))


      
