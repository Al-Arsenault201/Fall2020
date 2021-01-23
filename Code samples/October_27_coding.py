#coding from lecture of Monday, October 26

dogs = { "doug": ["beagle","bulldog"], "lizzie": "Australian cattle dog", "penny": "spaniel", "bonnie":"beagle", "remy":"shepherd"}

governors = {"Maryland": "Hogan", "Virginia":"Northam", "Louisiana":"Edwards"}

recipe = {'butter':2, 'flour':1.5,'salt':1,'Soda':1, 'Granulated sugar':0.25, 'brown sugar':1, 'egg':2,
         'milk':2, 'vanilla':1.5,'Chocolate chips':12}

eggs = int(input("how many eggs do you have?"))
if eggs < recipe["egg"]:
	print("Add a dozen eggs to your grocery list")

chips = int(input("how many ounces of chocolate chips do you have?"))
if chips < recipe["Chocolate chips"]:
	print("Get a bag of chocolate chips at the store")



a = [1,2,3]
b = [4,5,6]
c = zip(a, b)
d = dict(c)

with open("fall_2021.txt", "r") as f:
    useless_line = f.readline()
    useless_line = f.readline()
    data = f.readline()
    data = data.split()
    name = data[0] + data[1]
    scores = []
    for i in range(3, len(data)):
        scores.append(int(data[i]))
    data_dict = {}
    data_dict[name]= scores

