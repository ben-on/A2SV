x=input()

lst=x.split()
a=int(lst[0])
b=int(lst[1])
c=int(lst[2])
d=0
e=0
if a%c==0:
    d=a//c
else :
    d=(a//c)+1
if b%c==0:
    e=b//c
else :
    e=(b//c)+1
print(d+e)
