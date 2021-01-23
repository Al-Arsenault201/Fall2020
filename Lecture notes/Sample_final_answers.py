# problem 22
"""
Supposed you have a string representing course letter grades that looks like: grades = "A,B,C,A,A,B,A,B,A".
Write a Python function 'clean_up' that takes this string as input and returns a
string with the grades separated by one blank space each; that is, it returns "A B C A A B A B A".
Hint: think about how you'd use split and join.
"""

def clean_up(instring):
    # first split the string into a list on the commas
    temp_list = instring.split(',')
    # now create the new string with spaces separating the elements
    outstring = " ".join(temp_list)
    return outstring


#problem 23
"""
Write a Python function, step_search that implements a new search algorithm. 
The function should take two parameters: a list of integers to be searched; and target, an integer
 that is the value for which we are searching. The pseudcode for step_search is: 
 (a) calculate 
 the step_size as the square root of the length of num_list. You may assume that the math module 
 has been imported and you may use math.sqrt() to compute this value. 
 (b) Start a loop. Each time through the loop, ""jump"" to the list element ""step_size"" 
 places up the list from the previous one. Check to see if this element is greater than the target. 
 If so, fall out of the loop. Otherwise keep jumping up. If you hit the end of the list, 
 return -1. 
 (c) Once you have a list element that is greater than target, start at that 
 element and work backwards one step-size. That is, check each of the elements from the starting 
 point back to one step_size smaller. If you find the target, return its index in the list. 
 If you have checked each of these elements and not found the target, return -1.

"""
def step_search(inlist, target):
    # initialize the variables we need in the search
    step_size = int(math.sqrt(len(inlist)))
    i = 0
    found = False

    # now look to see if any item in the list is larger than the target
    # if not return -1
    while not found and i < len(inlist):
        if inlist(i) == target:
            return i
        elif inlist(i) > target:
            found = True
        else:
            i += step_size
    if not found:
        return -1

    # the following code assumes found == True
    # that is, inlist[i] > target for some i
    # now we need to walk back looking at each item for the target
    j = i
    while j > i - step_size:
        if inlist[j] == target:
            return j
        else:
            j -= 1
    return -1

#problem 24
"""
Write a Python program that reads three lists, A, B, and C, from three different files, A.dat, 
B.data and C.dat. A, B, and C all contain strings, and each is the same length. 
Convert these three lists into a single list, combined, that contains all of the data. 
The data from A should be in the first column of combined, with the data from B in the middle 
column and the data from C in the last column

"""
#first read the data in
with open("A.dat", "r") as f:
    A = f.readlines()
with open ("B.data", "r") as g:
    B = g.readlines()
with open ("C.dat","r") as h:
    C = h.readlines()

# now combine the three lists into a single 2-D list.
# since everything is a string, and A, B and C are lists
# of strings, there is no need to do any type conversion

combined_list = []

# All the lists are the same length
#so it doesn't matter which one we use to control the for loop
for i in range(len(A)):
    temp = []
    temp.append(A[i])
    temp.append(B[i])
    temp.append(C[i])

    #now add the row to the combined list
    combined_list.append(temp)


#problem 25
"""
Write a Python function, split_it that takes as parameters a string, and an integer 
indicating how long each substring should be. The function must return the list of substrings. 
For example, if the string is ""Go Saints"" and the integer is 1, you must return 
['G','o',' ','S','a','i','n','t','s'] while if the integer is 2 you must return 
['Go',' S', 'ai', 'nt', 's']. (The last substring may be shorter.)


"""

def split_it(instring, length):
    substring_list = []
    i = 0
    while i < len(instring):
        if i + length <= len(instring):
            substring_list.append(instring[i:i+length])
        else:
            substring_list.append(instring[i:])
        i += length
    return substring_list


