n=10
i=1
while(i<=n):
    if(i==1):
        print(i,"not prime")
    x=2    
    while(x<i):
        if(i%x==0):        
           print(i,"not prime")
           break
        x=x+1
    if(x==i):
        print(i,"prime")
    i=i+1    
