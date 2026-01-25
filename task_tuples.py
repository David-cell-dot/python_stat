#1. numbers = (10, 20, 30, 40, 50)Add 60 to the end,Replace 30 with 35.
#2. values = (15, 5, 30, 25, 10) arrange the elements in ascending order.
#3. fruits = ("apple", "banana", "cherry", "banana", "mango", "banana")
#Countoccurrences of "banana",Remove all occurrences of "banana".
#4. names = ("Alice", "Bob", "Charlie", "David") Reverse the order of elements using sort method.
#5. colors = ("red", "blue", "green")add "yellow" at index 1,Extend with ["purple", "orange"]


#question 1
numbers=(10, 20, 30, 40, 50)# add 60 at the end and replace 30 with 35
numbers=list(numbers)
print(numbers)#[10, 20, 30, 40, 50]
numbers.append(60)
print(numbers) # #append method
numbers=[10, 20, 30, 40, 50]
numbers=numbers.append(60)
print(numbers)#[10, 20, 30, 40, 50, 60]

#replace 30 with 35
numbers=[10, 20, 30, 40, 50, 60]
numbers.pop(2)
print(numbers)#[10, 20, 40, 50, 60]
numbers.insert(2,35)
print(numbers)#[10, 20, 35, 40, 50, 60]
numbers=tuple(numbers)
print(numbers)#(10, 20, 35, 40, 50, 60)

#question 2 sort in ascending order
values = (15, 5, 30, 25, 10) 
values=list(values)
print(values)#[15, 5, 30, 25, 10]
values.sort()
print(values)#[5, 10, 15, 25, 30]

values=tuple(values)
print(values)#(5, 10, 15, 25, 30)

#question 3
#Count occurrences of "banana",Remove all occurrences of "banana".
fruits = ("apple", "banana", "cherry", "banana", "mango", "banana")
fruits=list(fruits)
print(fruits)#['apple', 'banana', 'cherry', 'banana', 'mango', 'banana']
fruits=fruits.count("banana")
print(fruits)#3

#remove
fruits=['apple', 'banana', 'cherry', 'banana', 'mango', 'banana']
fruits.remove("banana")
fruits.remove("banana")
fruits.remove("banana")
print(fruits)

fruits=tuple(fruits)
print(fruits)#('apple', 'cherry', 'mango')

#question 4
# Reverse the order of elements using sort method
names = ("Alice", "Bob", "Charlie", "David")
names=list(names)

print(names)#['Alice', 'Bob', 'Charlie', 'David']

#sort
names=['Alice', 'Bob', 'Charlie', 'David']
names.sort()
print(names)#['Alice', 'Bob', 'Charlie', 'David']
names=tuple(names)
print(names)#('Alice', 'Bob', 'Charlie', 'David')

#question 5,add and extend
#add "yellow" at index 1,Extend with ["purple", "orange"]
colors = ("red", "blue", "green")
colors=list(colors)
print(colors)#['red', 'blue', 'green']

colors=['red', 'blue', 'green']
colors[1]='yellow'
print(colors)#['red', 'yellow', 'green']

#extend with purple,orange
colors=['red', 'yellow', 'green']
text=['purple','orange']
colors.extend(text)
print(colors)#['red', 'yellow', 'green', 'purple', 'orange']

colors=tuple(colors)
print(colors)#('red', 'yellow', 'green', 'purple', 'orange')