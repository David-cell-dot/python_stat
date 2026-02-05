#Take three inputs from a user, separately. Print the largest of the numbers.
   # Hint: Determine what type of data is taken in as input.
#2.Take as input from a user the temperature if the temperature is above 30°C display
#  “The temperature is too high”,if the temperature is above 15 display 
# “Normal temperature” otherwise display “Cold temperature”
#3.	Write a Python program that checks if a variable x is between 10 and 20 (inclusive)
#and if another variable y is greater than 100. If both conditions are true, print 
# "Conditions met", otherwise print "Conditions not met"
#4. Write a Python program that checks if a variable password is equal to the string "secret123". 
#  it is, print "Access   granted", otherwise print "Access denied"
#5. Write a Python program that checks if a variable student_score is greater than 90. 
# If true, check if the attendance is greater than 80. If b


#question 1
x=3
y=4
z=5

x=int(input(" enter a number:"))
y=int(input("enter a number:"))
z=int(input("enter a number:"))

if(x>y>z):
    print("x is the largest number")
elif y>z>x:
    print("y is the largest number")
else:
    print("z is the largest number")

##2.Take as input from a user the temperature if the temperature is above 30°C display
#  “The temperature is too high”,if the temperature is above 15 display 
# “Normal temperature” otherwise display “Cold temperature”

temp=int(input(" enter the temperature:"))
if temp>=30:
    print("temperature is too high")
    
elif temp>=15:
    print("normal temperatue")

else:
    print("cold temperatue")




##3.	Write a Python program that checks if a variable x is between 10 and 20 (inclusive)
#and if another variable y is greater than 100. If both conditions are true, print 
# "Conditions met", otherwise print "Conditions not met"

x=20
x=10
y>100

if x >=10 & x <=20 & y>100:
    print("condition met")
else:
    print("condition not met")



##4. Write a Python program that checks if a variable password is equal to the string "secret123". 
#  it is, print "Access   granted", otherwise print "Access denied"


password=input("enter a password:")

if password=="secret123":
    print("access")
else:
    print(" Access Denied")


 


#5. Write a Python program that checks if a variable student_score is greater than 90. 
# If true, check if the attendance is greater than 80. If both conditions are true, 
# print "Excellent student", otherwise print "Good score, but attendance needs improvement"

student_score = int(input("enter student marks:"))
student_attendance=int(input(" enter student attendance"))

if student_score>=90 & student_attendance>=80:
    print(" Excellent student")
else:
    print("Good score,But attendance needs improvement: ")





#Take four inputs from a user, separately. Print the largest of the numbers.
   # Hint: Determine what type of data is taken in as input.

value1=int(input(" enter the value"))
value2=int(input(" enter the value"))
value3=int(input(" enter the value"))
value4=int(input(" enter the value"))


if value1>value2 and value1>value3 and value1 >value4:
    print(f"{value1} is the largesr")
elif value2>value1 and value2>value3 and value2>value4:
    print(f"{value2} is the largesr") 
elif value3>value1 and value3>value2 and value3 > value4:
   print(f"{value3} is the largesr") 
elif value4>value1 and value4>value2 and value4 > value3:
   print(f"{value4} is the largesr")
    




   