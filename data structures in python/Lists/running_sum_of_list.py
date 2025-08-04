# find running sum of array 
# i/p->2 3 4 5
# o/p->2 5 9 14
l=list(map(int,input().split()))
for i in range(1,len(l)):
    l[i]=l[i]+l[i-1]
print(l)
