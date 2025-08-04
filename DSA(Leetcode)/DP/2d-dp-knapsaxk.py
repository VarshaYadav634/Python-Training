wt=[1,2,4,3]
pr=[5,8,13,9]
W=5
dp=[[0]*(W+1) for i in range(len(wt))]
for j in range(W+1):
    if wt[0]<=j:
        dp[0][j]=pr[0]
    else:
        dp[0][j]=0
for i in range(1,len(wt)):
    for j in range(W+1):
        if wt[i]>j:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j],pr[i]+dp[i-1][j-wt[i]])
for i in range(len(wt)):
    print(dp[i])