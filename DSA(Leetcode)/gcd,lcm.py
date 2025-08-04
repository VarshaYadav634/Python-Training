"""
20: 2,4,5,10
12: 2,3,4,6
"""
# GCD->Greatest common divisor
# a,b=map(int,input().split())
# gcd=1
# for i in range(1,min(a,b)+1):
#     if a%i==0 and b%i==0:
#         gcd=i
# print(gcd)

# or

"""
20: 2,4,5,10
12: 2,3,4,6
 
gcd(20,12)->a=b b=a%b gcd(12,8)->gcd(8,4)->gcd(4,0)
"""
# Eucledian Algorithm
# def gcd(a,b):
#     while b!=0:
#         a,b=b,a%b
#     return a
# a,b=map(int,input().split())
# print(gcd(a,b))


# LCM(least common multiple)
"""
20: 2,4,5,10
12: 2,3,4,6
 
lcm with euclidean algo
lcm(a,b)=(a*b)/gcd(a,b)
"""
def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
a,b=map(int,input().split())
print((a*b)//gcd(a,b))