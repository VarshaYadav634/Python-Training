# n=int(input())
# for i in range(n):
#     for j in range(i+1):
#         print(j+1,end=" ")
#     print()


# last line have all columns
n=int(input())
a=1
for i in range(n):
    if i==n-1:
        for j in range(n):
            print(a*a,end=" ")
            a+=1
    else:
        print(a*a,end=" ")
        a+=1
    print()