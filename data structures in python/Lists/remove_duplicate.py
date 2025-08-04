l=list(map(int,input().split()))
i=0
while i<len(l)-1:
    if l[i]==l[i+1]:
        l.pop(i+1)
    else:
        i+=1
print(l)