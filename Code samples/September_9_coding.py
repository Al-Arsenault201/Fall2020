#  This is the code developed in class on September 9

# Pseudocode: we will write a program that
# prompts the users for the grade, and the
# number of semester hours, for each class they
# took last semester.  Then we will calculate
# the student's semester GPA

# Assume we know you took 5 classes:
# Math, Chemistry, CompSci, Music, Bio
# We need to get the grade and number of
# of hours for each class

# in Python, anything input from the keyboard
# is a string.

# if you want it to be an integer
# you have to 'cast' it - change its type

math_grade = int(input("Enter your grade in Math"))
chem_grade = int(input("Enter your Chemistry Grade"))
cs_grade = int(input("Enter your CompSci Grade"))
music_grade = int(input ("Enter your Music Grade"))
bio_grade = int(input ("Enter your Bio Grade"))


# the above are assignment statements
# they assign a value to a variable name
# left-hand side and right-hand side
# - of the = sign

math_hours = int(input("how many hours was math?"))
cs_hours = int(input("how many hours was cs?"))
chem_hours = int(input("How many hours was chem?"))
music_hours = int(input("How many hours was music?"))
bio_hours = int(input("how many hours was bio?"))

total_hours = math_hours + cs_hours + chem_hours + music_hours + bio_hours

# calculate the number of quality points you got
# for each of the 5 classes

# quality points = hours times grade
math_points = math_hours * math_grade
chem_points = chem_hours * chem_grade
bio_points = bio_hours * bio_grade
music_points = music_hours * music_grade
cs_point = cs_hours * cs_grade

# semester GPA = total number of points
# divided by total number of hours

gpa = (math_points + chem_points +cs_point + bio_points + music_points) / (math_hours + music_hours + chem_hours + cs_hours + bio_hours)

# print out the result
print("The student GPA is ",gpa)