l = [0,1,2,2,3,0,4,2]
val = 2
i=0
while i<len(l):
    if l[i]==val:
        l.pop(i)
    else:
        i+=1
print(l)