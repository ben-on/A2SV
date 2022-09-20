
tastes=int(input())
for taste in range(tastes):
    t=int(input())
    lst=input().split()
    lst=[int(e) for e in lst]
    dp=[0]*t
    for i in range(t-1,-1,-1):
        # print(i,lst[i])
        dp[i]+=lst[i]
        move=i+lst[i]
        if move<t:
            dp[i]+=dp[move]
    print(max(dp))
    