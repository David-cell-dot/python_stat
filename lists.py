my_list=["mangoes","Oranges" ," pineaples",100,600,True,False]
print(my_list[0])
print(type(my_list))
DAYS=["monday","Tuesday","Wednesday","Thursady","Friday","Saturday","Sunday"]
print(DAYS[2])




#indexing
content=['mon','tue',['jan','feb','may' ], 'Wed',['nov','Oct','dec'],'Thur','fri']
print(content[2][2])
print(content[4][1])

content=['mon','tue','wed' 'Thur','fri']
content[3]="THURSDAY"
print(content)
# sort method
numbers=[10,20,40,80,89,22,45]
numbers.sort(reverse=False)
print(numbers)

#extend
vowels=["a","e","i","o","u"]
numbers=[10,20,40,80,89,22,45]
vowels.extend(numbers)
print(vowels)

#pop
numbers=[10,20,40,80,89,22,45]
numbers.pop()
print(numbers)

#remove
numbers=[10,20,40,80,89,22,45]
numbers.remove(20)
print(numbers)



#reverse
numbers.reverse()
print(numbers)

# check in
numbers=[1,5,7,9,10]
print(10 in numbers)

#count
print(numbers.count(7))



