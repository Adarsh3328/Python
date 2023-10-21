a=12
b=15
c=67
# a,b,c=12,15,67 single line input
if(a+b>c):
    if(b+c>a):
        if(c+a>b):
            print("valid triangle")
        else:
            print("invalid triangle")
    else:
         print("invalid triangle")
else:
     print("invalid triangle")