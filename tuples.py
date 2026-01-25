students=("alex","mike","james","mary","luke")
# add "john " between mary and luke
print(type(students))
students=list(students)
print(students)#['alex', 'mike', 'james', 'mary', 'luke']
students.insert(4,"john")
students=list(students)
print(students)

days=("monday","tuesday","wednesday","thursday","friday","saturday","sunday")
days=list(days)
print(days)# ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
print(days[2])
print(len(days))
days[3]="Thur"
print(days)
days=tuple(days)
print(days)