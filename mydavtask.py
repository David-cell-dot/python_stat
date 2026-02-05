##my_ds = [23, “Jane”, (560), [“Lesson”, “Maths”, {“currency” : “KES”}], 987, (76,”John”)]

#1. Print KES
#2. Print 560
#3. Print Maths
#4. In the dictionary with the key currency, add another key “amount” with value 90
#5. Reverse 987 to 789 without using an inbuilt -method or Assigning 789 manually.
#     Hint: Strings can be reversed using [::]
#6. Change the name “John” to “Jane” . 

#print 560
my_ds = [23, 'Jane', (560), ['Lesson', 'Maths', {'currency' : 'KES'}], 987, (76,'John')]

print(my_ds[2])

# PRINT MATHS
print(my_ds[3][1])

#print KES

print(my_ds[3][2])#{'currency': 'KES'}
my_ds={'currency': 'KES'}
print(my_ds['currency'])#KES

#In the dictionary with the key currency, add another key “amount” with value 90
my_ds[3][2]['amount']=90
print(my_ds)

#REVERSE 987 TO 789
print(my_ds[4])
my_ds[4]=str(my_ds[4])
my_ds[4]=my_ds[4][::-1]
my_ds[4]=int(my_ds[4])

print(my_ds)

# Change the name “John” to “Jane”  Change the name “John” to “Jane” 
my_ds[5]=list(my_ds[5])
my_ds[5][1]='jane'
print(my_ds)



