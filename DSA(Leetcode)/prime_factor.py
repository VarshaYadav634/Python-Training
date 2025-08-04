'''given an integer n, find all unique prime factors of n.
 
ip= 26
op= [2,13] '''

# n=int(input())
# l=[]
# for i in range(2,(n//2)+1):
#     if n%i==0:
#         ct=0
#         for j in range(1,i+1):  
#            if i%j==0:
#                ct+=1
#         if ct==2:
#             l.append(i)
# print(l)

# or


'''
given an integer n, find all unique prime factors of n.
 
ip= 26
op= [2,13]
 
ip= 100
op= [2,5]
'''
# def checkprime(n):
#     if n==1:
#         return False
#     if n==2:
#         return True
#     for i in range(2,n//2+1):
#         if n%i==0:
#             return False
#     return True
# number=int(input())
# res=[]
# for i in range(2,number//2+1):
#     if number%i==0 and checkprime(i):
#         res.append(i)
# print(res)


# or


'''
given an integer n, find all unique prime factors of n.
 
ip= 26
op= [2,13]
 
ip= 100
op= [2,5]
'''
# most optimized logic

n=int(input())
res=[]
if n%2==0:
    res.append(2)
    while n%2==0:
        n//=2
i=3
while i*i<=n:
    if n%i==0:
        res.append(i)
        while n%i==0:
            n//=i
    i+=2
if n>2:
    res.append(n)
print(res)
