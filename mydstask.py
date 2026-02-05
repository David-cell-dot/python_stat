#my_ds = [23, “Jane”, (560), [“Lesson”, “Maths”, {“currency” : “KES”}], 987, (76,”John”)]
#1. Print KES
#2. Print 560
#3. Print Maths
#4. In the dictionary with the key currency, add another key “amount” with value 90
#5. Reverse 987 to 789 without using an inbuilt -method or Assigning 789 manually.
#     Hint: Strings can be reversed using [::]
#6. Change the name “John” to “Jane” . 


my_ds = [23, 'Jane', (560), ['Lesson', 'Maths', {'currency' : 'KES'}], 987, (76,'John')]

#print KES
print(my_ds[3][2])#{'currency': 'KES'}
my_ds={'currency': 'KES'}
print(my_ds['currency'])#KES


#Print 560
# let my_ds[2]=(560)
X=str(560)
X=int("560")
print(X)#560

my_ds=X
print(my_ds)

#print maths
print(my_ds[3][1])
