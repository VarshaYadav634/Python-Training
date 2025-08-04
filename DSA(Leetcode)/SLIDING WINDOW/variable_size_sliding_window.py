# find the smallest subarray whose sum is greater than given target value
l=list(map(int,input().split()))
target=int(input())
curr_sum=0
n=len(l)
min_len=n+1
start=0
for end in range(n):
    curr_sum+=l[end]
    while curr_sum>target:
        min_len=min(min_len,end-start+1)
        curr_sum-=l[start]
        start+=1
print(min_len)