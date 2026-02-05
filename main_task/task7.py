#Write that prompts the user to input student marks.
#  The input should be between 0 and 100.Then output the correct grade: 
#A > 79 , B - 60 to 79, C  > 49 to 59, D - 40 to 49, E - less 40







def student_marks(maks):
   
    if maks>=79 and maks<=100:
        res="grade A"
    elif maks>=60 and maks<=79:
        res='grade B'
    elif maks>=49 and maks<=59:
        res='grade C'
    elif maks>=40 and maks<=49:
         res='grade D'
    else:
        res="grade E"

    return res


marks=input("enter marks:")
marks=int(marks)
student=student_marks(marks)
print(student)
       


