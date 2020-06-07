#rod cutting problem
length=int(input("Enter the length of rod:"))
ln=[]
price=[]
print("Enter the lenghts:")
for i in range(length):
    ln.append(int(input()))
print("Enter the prices:")
for i in range(length):
    price.append(int(input()))
print("length array:",ln)
print("price array:",price)
t=[[0 for i in range(length+1)]for j in range(length+1)]
for i in range(length+1):#n
   for j in range(length+1):
       if (ln[i-1]<=j):
           t[i][j]=max(price[i-1]+t[i][j-ln[i-1]], t[i-1][j])
       elif (ln[i-1]>j):
            t[i][j]=t[i-1][j]
        

print("maximum price:",t[i][j])
                       
   
   
    
