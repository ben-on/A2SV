t=int(input())
for r in range(t):
    n=int(input())
    lst=input().split()
    var=len(set(lst))
    for k in range(1,n+1):
        if k <= var:
            print(var,end=" ")
        else:
            print(k,end=" ")
    print()
            
        
    

                
        
    
    
    
    
    