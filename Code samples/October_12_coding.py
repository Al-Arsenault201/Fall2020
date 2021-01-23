# programming with functions

def print_error_message(code):
    if code == 0:
        print("You cannot divide by 0")
    elif code < 1 or code > 10:
        print("Only integers between 1 and 10 are valid")
    else:
        print("That is some other error")
    return

if __name__ == "__main__":
    print("This program divides 100 by an integer of your choice")
    value = int(input("please enter an integer between 1 and 10 inclusive"))
    if not(value >=1 and value <=10):
        print_error_message(value)
    else:
        print("your answer is ", 100/value)


def calculate_days (years, months, days):
    print("years is ",years, " months is ", months, " and days is ", days)
    num_days = 365 * years + 30 * months + days
    if years > 4:
        num_days += 1
    return num_days  # will be passed associated with the value of the function name

if __name__ == "__main__":

# def main(): don't worry about; don't use it with Python 3.8

    # find out how many years, months and days old someone is
    # convert it to days by calling the function calculate_days

    yrs = 23
    mos = 11
    days = 15

    age_in_days = calculate_days(yrs, mos, days)
    print("Your age is", age_in_days)


def subtract(x, y):
    print(x,'-',y,'=',str(x-y))
if __name__ == '__main__':
    x = 3
    y = 4
    subtract(y, x)
