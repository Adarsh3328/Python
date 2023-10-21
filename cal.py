n1=int(input("enter 1 value\n"))
while True:
        print("press any one 1,2,3,4,5\n")
        n2=int(input("1->+ 2->- 3->* 4->/ 5->%\n"))
        n3=int(input("enter 2 value\n"))
        if(n2==1):
            n4=n1+n3
        if(n2==2):
            n4=n1-n3
        if(n2==3):
            n4=n1*n3
        if(n2==4):
            n4=n1/n3
        if(n2==5):
            n4=n1%n3
        print(n4)
        n1=n4
        nextoper=input("if you want quit press N if you continue with same operations press enter\n")
        if(nextoper=='n'):
            break                    
