l=list(map(int,input().split()))
k=int(input())
n=len(l)
for i in range(n-2):
    left=i+1
    right=n-1
    flag=True
    while left<right:
        if(l[left]+l[right]+l[i]==k):
            print(i,left,right)
            flag=False
            break
        elif l[left]+l[right]+l[i]>k:
            right-=1
        else:
            left+=1
    if flag==False:
        break