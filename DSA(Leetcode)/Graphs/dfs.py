def dfs(d,start,vis):
    vis.add(start)
    print(start)
    for i in d[start]:
        if i not in vis:
            dfs(d,i,vis)
 
d = {0: [1,4], 1: [2,3,4],2: [2,3,4],3: [1, 2, 4], 4: [2, 3]}
dfs(d,0,set())