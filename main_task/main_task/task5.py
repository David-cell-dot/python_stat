#Implement a program that takes 3 users  inputs from the terminal or the Browser, 
# and stores them in three variables. Return the largest of the three.
#  Do this without using the the inbuilt max () function!




def largest_number(x,y,z):
  



    if x>y and x>z:
        res=f"{x} is the largest"
    elif y>x and y>z:
        res=f"{y} is the largest"
    else:
        res=f"{z} is the largest"
        

    return res
    
num1=input(" enter value ")
num2=input(" enter value ")
num3=input(" enter value ")
num1=int(num1)
num2=int(num2)
num3=int(num3)

result=largest_number(num1,num2,num3)
print(result)
