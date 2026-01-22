#name = “  JOHn  .“ to “john”
name ="   JOHn  . "
name=name.replace("." ," ")
name=name.strip()
name=name.lower()
print(name)


#question2
#sentence_one = “The Dog Breed is German Shepherd” only display “Breed is German”
sentence_one = "The Dog Breed is German Shepherd"
sentence_one=sentence_one[8:23]
print(sentence_one)

#sentence_two = “Defeats for the Clinton forces, this was her moment of triumph” only display “Clinton forces”
sentence_two= "Defeats for the Clinton forces, this was her moment of triumph"
print(sentence_two[ 16:30])

#split using semicolon
#“The lazy dog; ran so fast; it hit the wall.” 
sentence="The lazy dog; ran so fast; it hit the wall."
print(sentence.split(";"))
print(len(sentence))












#first_name="  Joh.n"  last_name="   Do,e" Clean up and display Full name i.e John Doe
first_name="   Joh.n"
first_name=first_name.strip()
first_name=first_name.replace(".","")
print(first_name)

#last-name  ="   Do,e"
last_name="   Do,e"
last_name=last_name.strip()
last_name=last_name.replace("Do,e", " Doe")
print(last_name)

# concatenate
full_name =first_name+ " "+ last_name
print(full_name)


#Having the string r = '[["E","W","C"]]' #Manipulate it to display EWC
r = '[ "E","W","C" ]'
r=r.replace(" ' " ," ")
r=r.replace("[" ," ")
r=r.replace("," ," ")
r=r.replace(" ]" ," ")
r=r.replace(" " " ", " ")
r=r.replace(" ""  " ," ")

print(r)
#r = '[ "E","W","C" ]'
s='[ "E","W","C" ]' 
s=s.split[2:11]

print(s)
  