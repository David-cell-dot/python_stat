categories = ['Fruit', 'Vegetable']
foods = ['Apple', 'Carrot', 'Banana']

for category in categories:
    for food in foods:
        print(category, food)
           
developer_names = ['Jess', 'Naomi', 'Tom']
for developer in developer_names:
    if developer =="Naomi":
        continue
    print(developer)


    words = ['sky', 'apple', 'rhythm', 'fly', 'orange']

for word in words:
    for letter in word:
        if letter.lower() in 'aeiou':
            print(f"'{word}' contains the vowel '{letter}'")
            break
    else:
        print(f"'{word}' has no vowels")




        
for num in range(2, 11, 2):
         print(num)


for num in range(40, 0, -10):
      print(num)