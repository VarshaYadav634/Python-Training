# n=input()
# print(n[::-1])

n=int(input())
rev=0
while n!=0:#256, 25, 2
    rem=n%10  #6, 5, 2
    rev=rev*10+rem #0*10+6=6*10+5=65*10+2=652
    n=n//10  #25, 2, 0
print(rev)


