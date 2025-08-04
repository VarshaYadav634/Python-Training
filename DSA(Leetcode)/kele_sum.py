'''consider sorted list and k integer. you have to find two elements whose addition is equal to k'''
l=[2,3,5,8,10]
k=11
left=0
right=len(l)-1
while left<right:
    if l[left]+l[right]==k:
        print(left,right)
        break
    elif l[left]+l[right]>k:
        right-=1
    else:
        left+=1
else:
    print("ele not found")

