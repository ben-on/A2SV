def main(lst):
    small=lst[0]+lst[1]
    s=1
    large=lst[-1]
    l=len(lst)-1
    while s<l:
        if small<large:
            return "YES"
        s+=1
        small+=lst[s]
        l-=1
        large+=lst[l] 
    return "NO"
no=int(input())
for i in range(no):
    n=input()
    lstt=input().split()
    lstt=[int(num) for num in lstt]
    lstt.sort()
    print(main(lstt))


                
        
    
    
    
    
    