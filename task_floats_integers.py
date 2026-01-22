#Convert a float to an integer with an inbuilt function in Python
#temp = 56.8926 to 57

t=56.8926

print(round(t))

#Convert the float below to give the results as follows
#temp = 56.8926 to 56.89 
temp=56.8926
print(round(temp,2))

#Convert the float below to give the results as follows
#temp = 56.8926 to 56.893
tem= 56.8926
print(round(tem,3))

#Convert the float below to give the results as follows
#temp=56.8926 to 8.926
temp= 56.8926
temp=str(temp)
print(temp)
# slice
slice_temp=temp[3:7]
print(slice_temp)

# concat
final_temp=slice_temp[0]+ " ."+slice_temp[1:4]

# convert to float
final_temp=float(final_temp)
print(final_temp)







