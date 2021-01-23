#Code discussed in Wednesday, September 23 lecture

# For loops

# a simple for each loop
grocery_list = ["Milk", "Eggs", "Cereal", "Coffee", "Apples", "Strawberries", "Broccoli", "Cucumber", "Tomatoes", "Green Onions"]
for item in grocery_list:
    print(item, end='')
    print(item)
income = int(input("Enter your current salary"))
rise = float(input("Enter the percentage your salary will increase each year"))
rate_of_return = float(input("Enter the annual rate of return you expect"))
savings = float(input("What percentage of your salary will you save every year?"))
years = int(input("How many years until retirement?"))

#income = 100000
#rise = 3
#rate_of_return = 7.75
#savings = 22
#years = 30
# Use a for i loop to calculate the amount you have
# each year
ira_balance = [income*savings/100]
for i in range(1,years):
    new_amount = ira_balance[i-1] + ira_balance[i-1]*(rate_of_return/100) + income*(savings/100)
#    print("new amount in year ", i, "is ", new_amount)
    ira_balance.append(new_amount)
    income *= (1+rise/100)

# Now a for each loop to print out the total you have
# after each year

for year in ira_balance:
    print(f"Your next balance is $ {year: .2f} ")

# and a "for i" loop to do the same

for i in range(1,years):
    year = ira_balance[i]
    print(f"Your balance after year {i: 3d} is $ {year: .2f}")

# nested for loops

for row in range(6):
    for column in range (4):
        print(row*column, end='  ')
    print('\n')




