l=list(map(int,input().split()))
for i in range(len(l)-1):
    min=l[i]
    mini=i
    for j in range(i+1,len(l)):
        if l[j]<min:
            min=l[j]
            mini=j
    l[i],l[mini]=l[mini],l[i]
print(l)