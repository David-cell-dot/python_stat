n=13
for i in range(1,4):
    for j in range(1,n+1):
        if (i+j)%4==0 or (i==2 and j%4==0):
            print("*", end=" ")
        else:
            print("",end="")


row=int(input("enter number of rows:"))
print("Generated hourglass pattern is:")
#upper_half
for i in range(row,0,-1):
    for j in range(row-1):
        print(" ",end="")
        for j in range(1,2*i):
            print("*",end="")
            print()





