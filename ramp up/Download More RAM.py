no=int(input())
for i in range(no):
    n,k=input().split()
    n,k=int(n),int(k)
    req=input().split()
    give=input().split()
    req,give=[int(i) for i in req],[int(i) for i in give]
    # print(req,give)
    goal=[""]*n
    for r in range(n):
        val=-float('inf')
        for j in range(n):
            if req[j]=="":
                continue
            if req[j]<=k:
                if give[j]>val:
                    val=give[j]
                    idx=j
        if val!=-float('inf'):
            k+=val
            req[idx]=""
    print(k)
    
    
    
    