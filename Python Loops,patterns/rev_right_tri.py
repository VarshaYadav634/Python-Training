n=int(input())
z=97
for i in range(n):
    for j in range(n-i):
        print(chr(z),end=" ")
        z+=1
    print()