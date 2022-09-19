t=int(input())
for r in range(t):
    s=input()
    one=False
    res=False
    for i in range(len(s)-1):
        if s[i]=='1' and s[i+1]=='1':
            one=True
        if s[i]=='0' and s[i+1]=='0' and one:
            res=True
    if not res:
        print("Yes")
    else:
        print("No")
            
         
        