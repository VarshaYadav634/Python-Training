# 24 is present in 2 table,4 table, upto 12 table.means a number have factor upto half of the value.
n=int(input())
for i in range(2,n//2+1):
    if n%i==0:
        print("not prime")
        break
else:
    print("prime")