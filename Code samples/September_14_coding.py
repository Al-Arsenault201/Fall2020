# Code covered in class on September 14

x = 7/3
print(x)

y = 7//3
print(y)

# whitespace means blank spaces, tabs, newlines
# characters that are used for spacing your python code

#whitespace around operators is ignored by python

#assignment statements
x= 0
x = x + 1

x += 1
x *= 4
x -= 3 # x = x - 3 NOT x = 3-x

a = True
print (a)

print(6 >= 5 + 2)

print (6 > 4 and 2 > 1)
print ('true'== True and 'false' == False)

# simplest conditional: if statement
gpa = 3.0
if (gpa >= 3.5):
# There MUST be at least one indented statement
    print("congratulations - Dean's list student")

# There are two cases in the conditional
if (gpa >= 3.5):
# There MUST be at least one indented statement
    print("congratulations - Dean's list
else:
    print('close but no cigar')

if (gpa >= 3.5):
# There MUST be at least one indented statement
    print("congratulations - Dean's list student")
    print("You did well this semester")
else:
    print('close but no cigar')
    print('better luck next semester')

# show how to input a letter grade and convert
# it to a number of quality points using conditionals

grade = input('Enter your grade in Math')
if grade == 'A' or grade == 'a':
    quality_points = 4
#elif is short for else if
elif grade == 'B' or grade == 'b':
    quality_points = 3
elif grade == 'C' or grade == 'c':
    quality_points = 2
elif grade == 'D' or grade == 'd':
    quality_points = 1
else:
    quality_points = 0