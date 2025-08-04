# accenture
rats_n=int(input())
food_per_rat=int(input())
total=rats_n*food_per_rat
houses_n=int(input())
l=list(map(int,input().split()))
i=0
while total>0:
    total=total-l[i]
    i+=1
    if(i==len(l) and total>0):
        print(-1)
        break
else:
    print(i)
            


