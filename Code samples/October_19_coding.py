# in-class coding from Monday, October 19

def build_name_list():
    name_list = []
    name = input("Enter a pet's name. Enter STOP to stop")
    while name != 'STOP':
        name_list.append(name)
        name = input("Enter a pet's name. Enter STOP to stop.")
    return(name_list)


def find_name_lengths(name_list):
    list_of_lengths = []
    for i in name_list:
        list_of_lengths.append(len(i))
    return list_of_lengths


def sum_lengths(length_list):
    sum = 0
    for i in length_list:
        sum += i
    return sum

if __name__ == "__main__":
    names = build_name_list()
    lengths = find_name_lengths(names)
    result = sum_lengths(lengths)
    print("The total length of the names in the list is: ", result)




with open("test_data.txt", "r") as f:
	data = f.read()  #reads in all data from the file as a single string
#	data_lines = f.readlines() # reads in all data from the file
							# returns a list of strings - each element in the
							#list is one line from the file
#	next_line = f.readline() #reads in one line from the file; returns it as a string

# example - read in a file of integers
# read in a file of integers, and print the largest integer
with open("integers.txt", "r") as f:
    data = f.read()
    numbers = data.split()
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])
    largest = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] > largest:
            largest = numbers[i]
    print("The largest integer in the file was ", largest)


with open("results.txt", "w") as out:
    s = "The largest input in the file was: " + str(largest)
    out.write(s)

with open('dogs_and_cats.txt','r') as f:
    content = f.read()
    contents = content.split()
    new_content = []
    for word in contents:
        if word == 'dog':
            new_content.append('cat')
        else:
            new_content.append(word)
# use join to create a string
s = " ".join(new_content)
with open('dogs_and_cats.txt', 'w') as out:
    out.write(s)
