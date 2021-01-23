

class Car:
   def __init__(self):
       self.make = 'Toyota'
       self.model = 'Camry'
       self.vin = '123412341234'
       self.license_plate = '3AB1234'


class Car:
   def __init__(self, make, model, id, license_plate):
       self.make =  make
       self.model = model
       self.vin =  id
       self.license_plate = license_plate

my_car = Car('Toyota', 'Corolla', '12345', 'GoDogs')

your_car = Car('Honda', 'CRV', '98765', 'GoTerps')

class Car:
   def __init__(self, make, model, id, license_plate):
       self.make =  make
       self.model = model
       self.vin =  id
       self.license_plate = license_plate
       self.passengers = []

   def add_passenger(self, passenger):
       self.passengers.append(passenger)


class Passenger:
    def __init__(self,name):
        self.name = name

eric = Passenger('Eric')
my_car.add_passenger(eric)


deposit = float(input("Enter deposit amount; 0.0 to stop"))
while deposit != 0.0:
    # do something
    deposit = float(input("Enter deposit amount; 0.0 to stop"))

for state in states:
    if state[-1] in ['a','e','i','o','u']:


def read_file(filename):
    with open (filename, "r") as f:
        city_list = f.readlines()
        for i in range(len(city_list)):
            city_list[i] =city_list[i].split()
            city_list[i][1] = float(city_list[i][1])
        return city_list

if __name__ == "__main__":
    c_list = read_file("cities.txt")
    pops = c_list[1]
    pops.sort()
#    pops[-1]  #has the largest population - find that city
    for i in range(len(c_list)):
        if c_list[i][1] == pops[-1]:
            print("The largest city is ", c_list[0], 'with a population of ', c_list[1])





nums = [5,4,8,7,2,1]
nums.sort()
