a,b=input("").split()
a=int(a)
b=int(b)
if b%2==0:
    c=a*(b/2)
elif a%2==0:
    c=b*(a/2)
else :
    c=(a*(b//2))+(a//2)


print(int(c))
