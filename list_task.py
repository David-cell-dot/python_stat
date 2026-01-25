#create a new file list_task.py
#trainees = ["John", [2, ["James","Mary"]]]
# Display 2 from the list.
trainees=["John", [2, ["James","Mary"]]]
print(trainees[1][0])
#Output James  from the list.
print(trainees[1][1][0])

# Using a method add 56 at the end of the list.
trainees=["John", [2, ["James","Mary"]]]
t=[56]
trainees.append(t)
print(trainees)# ['John', [2, ['James', 'Mary']], [56]]

trainees=['John', [2, ['James', 'Mary']], [56]]
trainees[1][1][1:0]=["MIKE"]
#trainees[1][1].insert(1,"mike")
print(trainees)# ['John', [2, ['James', 'MIKE', 'Mary']], [56]]


# Change the value of 2 to 8
trainees[1][0]=8
print(trainees)

#remove john#['John', [8, ['James', 'MIKE', 'Mary']], [56]]

trainees.pop(0)
print(trainees)

#remove mary#[[8, ['James', 'MIKE', 'Mary']], [56]]
trainees[0[2]].pop
print(trainees)

