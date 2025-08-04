#Binary Search
 
l=list(map(int,input().split()))
se=int(input())
si=0
li=len(l)-1
while si<=li:
    mid=(si+li)//2
    if(l[mid]==se):       
        print("element found")
        break
    elif se>l[mid]:
        si=mid+1
    else:
        li=mid-1
else:
    print("element is not present")