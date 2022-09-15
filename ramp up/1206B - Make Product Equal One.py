t=int(input())
lst=input().split()
lst=[int(i) for i in lst]
neg=0
res=0
zeros=0
for i,val in enumerate(lst):
    if val<0:
        res+=-val-1
        neg+=1
    elif val>0:
        res+=val-1
    else:
        zeros+=1
if neg%2 and zeros==0:
    print(res+2)
else:
    print(res+zeros)
        