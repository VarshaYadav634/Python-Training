'''take an n integer from user and till n ,print all prime numbers'''
# n=int(input())
# res=[]
# if n==1:
#     print("not prime")
# else:
#     for i in range(2,n+1):
#         ct=0
#         for j in range(1,i+1):
#             if i%j==0:
#                 ct+=1
#         if ct==2:
#             res.append(i)
# print(res)

# or
# optimized logic

# Sieve of erasthones
n=11
d=[True]*(n+1)
d[0]=False
d[1]=False
i=2
 
while i*i<=n:
    if d[i]:
        for i in range(i*i,n+1,i):
            d[i]=False
    i+=1
 
res=[i for i in range(n+1) if d[i]]
print(res)

