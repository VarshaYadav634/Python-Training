n=int(input())
for i in range(n-1,-1,-1):
    for s in range(n-i-1):
        print(" ",end=" ")
    for j in range(i+i+1):
        print("*",end=" ")
    print()