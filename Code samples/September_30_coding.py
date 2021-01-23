import sys
from random import choice, seed

#if __name__ == "__main__":

# 10000001
# 11000001
age = 0;
while (age < 18):
	age = int(input("enter your age in years:")
	print ("If you’re 18 or older you should vote")
print ("that's the end of our story")

# factorial with a for loop
product = 1
number = int(input("what number should I calculate factorial for?"))
for i in range(1,number+1):
    product *= i
print(product)

# factorial with a while loop
product = 1
number = int(input("what number should I calculate factorial for?"))
index = 1
while (index <= number):
    product *= index
    index += 1
print(product)

grade = ""
name  = ""
while name != "Hrabowski":
    # get the user's grade
    grade = input("What is your grade? ")
print("You passed!")

cookiesLeft = 50

while cookiesLeft > 0:
    # eat a cookie
    cookiesLeft = cookiesLeft + 1

#print all the positive odd numbers
#less than 100

num = 1
while num != 100:
    print(num)
    num = num + 2

rth as mm/dd. Enter ‘Q’ to quit.")


birthdate = input("Enter your month and day of birth as mm/dd. Enter ‘Q’ to quit.")
while birthdate != "Q":
    month_and_day = birthdate.split('/')
    for i in range(2):
        month_and_day[i] = int(month_and_day[i])
    day_of_year = 30 * (month_and_day[0] -1) + month_and_day[1]
    print(f"Your birthday is the {day_of_year:5d} day of the year")
    birthdate = input("Enter your month and day of birth as mm/dd. Enter ‘Q’ to quit.")
