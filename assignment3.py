#Assignment
#Print the names Patricia, Phionah and Anitah
#Add masha at the 4th position
#Update the phionah to phionah aladina
#Display the length of the students list
# Print all the students name using a for loop
#Calculate the total marks for tghe student mark variable and the total mark is 304 

studentNames = ['Sandra','Patricia','Phiona', 'Anitah']
studentsMarks  = [80, 56, 78, 90]
print(studentNames)

studentNames.insert(4,'Masha')
print(studentNames)

studentNames[2] = "Phionah Aladinah"
print(studentNames)

total_length = len(studentNames)
print(f'The total length of the student list is: {total_length}')

for names in studentNames:
  print(names)

sum = (80 + 56 + 78 + 90)
print(f"The total mark is {sum} ")