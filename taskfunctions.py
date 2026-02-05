#Write a python program that takes from a user 5 inputs (maths, eng, swa, sci, sos). 
#Create a function that calculates the total marks another the average marks ,
# then a functions that finds the grade according to the table below. 

#Use the value from total to get the average and average to find the grade.

#A > 79 , B - 60 to 79, C -  59 to 49, D - 40 to 49, E - less 40


#question1
#Write a python program that takes from a user 5 inputs (maths, eng, swa, sci, sos). 
subects=input("enter the subject:")

#add_marks


def add_marks(maths,eng,swa,sci,sos):
    return maths +  eng + swa + sci +sos
result=add_marks(90,89,78,99,88)
print(result)


add_marks(90,89,90,78,99)



def get_average(maths,eng,swa,sci,sos):
    add_marks=[90,89,78,99,88]
    sum=0
    for i in add_marks:
        sum=sum+i
        return sum
    


    average=sum/len(add_marks)
    print(average)
    
get_average(90,89,78,99,88)



#square_number
def square_number(x):
    square=x**2

    return square
 
x=square_number(2)
print(x)


#cube_number(num)
def cube_number(y):
    cube=y**3
    return cube

cube=cube_number(4)
print(cube_number)


#add_numbers
def add_number(a,b):
    sum=a+ b
    return sum


value1=add_number(4,8)
print(value1)


def check_password(password):
    correct_password="secret123"
    if password==correct_password
        res="access granted"
    else:
        res="access denied"

    return  res

user_input=input("enter password:")
result=check_password("user_input")
print(result)






##Use the value from total to get the average and average to find the grade.

#A > 79 , B - 60 to 79, C -  59 to 49, D - 40 to 49, E - less 40

def get_average():

    if get_average>=79 and get_average<=100:
        print("grade A")
    elif get_average>=60 and get_average<=79:
        print("grade B")
    elif get_average>=50 and get_average<=59:
        print("grade C")
    elif get_average>=40 and get_average<=49:
        print("grade D")
    else:
        print("grade E")


get_average()










  







    
 
    
  
   

    




#Create a function that calculates the total marks another the average marks ,
# then a functions that finds the grade according to the table below. 

 





    

  
    
  

    
 


