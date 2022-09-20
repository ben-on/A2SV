n,k=input().split()
lst=input().split()
lst=[int(e) for e in lst]
n,k=int(n),int(k)
# print(lst)
res=0
for i in range(1,len(lst)):
    fract=k-lst[i]-lst[i-1]
    if fract >0:
        res+=fract
        lst[i]+=fract
print(res)
for i in lst:
    print(i,end=" ")