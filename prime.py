n=10
x=2
if(n==1):
    print("not prime")
while(x<n):
    if(n%x==0):
        print("not prime",x)
        break
    x=x+1
if(x==n):
    print("prime",x)
