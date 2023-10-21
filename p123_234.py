n1=int(input("Enter a number\n"))
print()# for new line
row=1
while(row<=n1):
    col=1
    val=row
    while(col<=n1):
        print(val,end=" ")
        val=val+1    
        print("\t", end=" ")
        col=col+1
    print()
    row=row+1    