my_dic={
    "name":"David Wafula",
    "age":39,
    "Location":"Bungoma",
    "name":"geofrey",
    "age":35,
    'city':"Nairobi"
}

print(my_dic)
print(type(my_dic))
print(my_dic["Location"])

#update values
my_dic["age"]=45
my_dic["name"]=" stano"
my_dic["city"]="doha"
my_dic["location"]="Kisumu"
print(my_dic)

#add values
my_dic["occupation"]="software"
my_dic["address"]=" 123 nairobi"

my_dic.pop("age")
print(my_dic)