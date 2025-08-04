# To find nth fibanocci number using dp
# In DP with the help of previous values we find present value
n=int(input())
l=[0]*(n+1)
for i in range(n+1):
    if i==0:
        continue
    elif i==1:
        l[1]=1
    else:
        l[i]=l[i-1]+l[i-2]
print(l[n])  
