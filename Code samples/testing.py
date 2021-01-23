import dates  #import all the functions in the program dates.py
if __name__ == "__main__":
    print(dates.convert_date('07042020')) #program name.function name

from dates import * #import everything from dates.py
#from dates import convert_date
if __name__ == "__main__":
    print(convert_date('07072020'))