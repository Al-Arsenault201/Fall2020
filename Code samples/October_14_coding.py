numbers =[]
for i in range(100, 89, -1):
    numbers.append(i)

a = bool(input("enter True or False"))
b = bool(input("enter True or False"))
if (a == True and b == False) or (a == False and b == True):
    xor = True
else:
    xor = False
print("The exclusive or value is: ", xor)

# Coding from October 14

def Factorial(num):
    # num is a positive integer; return that number factorial
    # num!
    product = 1
    print(" number is, ", number)
    for i in range(1, num+1):
        product *= i
    return(product) # return product

if __name__ == "__main__":
    number = 6
    fact = Factorial(number)
    print (number, " factorial is ", fact)

# the “fourth root” of a number is that number raised to the (¼) power
#
def fourth_root(num):
	ans = num**(1/4)
	return (ans)

#set the variable’s value, then call the function
original_number = 81
final_number = fourth_root(original_number)
print(final_number)


#  First the function definition
def reverse_word (word):
# now the code. DON’T FORGET TO INDENT!!
    i = 0
    reversed_word = ''  #Do not use the function name here!!!!
    while i < len(word):
        reversed_word = reversed_word + word[len(word)-1 - i]
        i += 1
    print (" The word ", word, " reversed is ", reversed_word)
    return (reversed_word)


#reverse_word("UMBC")
animals = ['dog','cat','cow', 'chicken']
for critter in animals:
    print(reverse_word(critter))