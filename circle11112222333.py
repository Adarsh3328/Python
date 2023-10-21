n1=int(input("Enter a number\n"))
print()# for new line
row=1
while(row<=n1):
    col=1
    while(col<=n1):
        print(min(row,col,n1-row+1,n1-col+1),end=" ")    
        print("\t", end=" ")
        col=col+1
    print("")
    row=row+1
    print("")    