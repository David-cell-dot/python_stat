fruits=["mango","banana","orange","lemon"]
for i in fruits:
    print(i)

# create  a list of from 40 to 50
#print your name 40 times




x=list(range(10,51))
print(x)
for i in x:
    print("david")



      
numbers=list(range(10,51))
odd_numbers=[]
for num in numbers:
    if num%2!=0:
        odd_numbers.append(num)



print(odd_numbers)

numbers=list(range(1,4))
for i in numbers:
    pin=input("enter pin:")
    correct_pn="5678"
    if pin==correct_pn:
        print("pin granted")
        break
    else:
        print("try again")



numbers=list(range(1,6))
for i in numbers:
    password=input("enter password:")
    correct_password="admin@123"
    if password==correct_password:
        print("access granted")
        break
    else:
         remaining_tries=5-i
         if remaining_tries==0:
             print("account blocked")
         else:
             print( f" try again,you have{remaining_tries} attempts remaining ")










person=("jane","python dev",25,"canada")
for field in person:
        print(field)




numbers=[1,3,5,7,9]
target=5
for numbers in numbers:
    print(f"processing{numbers} ....")
    if numbers==target:
        print(f"target found{target}!")
        break


numbers=[1,2,3,4,5,6]
for number in numbers:
    print(f"{number=}")
    if number%2!=0:
        continue
    print(f"{number} is even!")



for number in range(1,11):
    for product in range(number,number*11, number):
         print (f"{product:>4d}", end= "")
         print()







 




    










