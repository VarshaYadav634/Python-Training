'''
take a list from user and take k value and rotate k elements from list
 
l=[5,8,9,1,4,2]
k=3
 
1 4 2 5 8 9
'''
l=[5,8,9,1,4,2]
k=3
n=len(l)
for i in range(k):
    temp=l[0] #5
    for j in range(1,n):
        l[j-1]=l[j]
    l[n-1]=temp
print(l)