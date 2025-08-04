"""
take a number from user and find out factorial of a number
"""
# import numpy as np
# x=1000
# y=600
# print(np.prod(np.arange(y+1,x+1)))

# or

# recursions
# def fact(n):
#     if n==1:
#         return 1
#     return n*fact(n-1)
# print(fact(5))

# or

"""
take one int value from user and find factorial of all numbers from 1 to n
"""
n=int(input())
l=[1]*(n+1)
for i in range(2,n+1):
    l[i]=l[i-1]*i
print(l)

