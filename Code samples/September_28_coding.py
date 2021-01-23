#formatting output
x = 1/3
print(x)


states = ['Washington', 'Oregon', 'California', 'Ohio', 'Nebraska', 'Colorado', 'Michigan', 'Massachusetts', 'Florida', 'Texas', 'Oklahoma', 'Hawaii', 'Alaska', 'Utah', 'New Mexico', 'North Dakota', 'South Dakota', 'West Virginia', 'Virginia', 'New Jersey', 'Minnesota', 'Illinois', 'Indiana', 'Kentucky', 'Tennessee', 'Georgia', 'Alabama', 'Mississippi', 'North Carolina', 'South Carolina', 'Maine', 'Vermont', 'New Hampshire', 'Connecticut', 'Rhode Island', 'Wyoming', 'Montana', 'Kansas', 'Iowa', 'Pennsylvania', 'Maryland', 'Missouri', 'Arizona', 'Nevada', 'New York', 'Wisconsin', 'Delaware', 'Idaho', 'Arkansas', 'Louisiana']


capitals = ['Olympia', 'Salem', 'Sacramento', 'Columbus', 'Lincoln', 'Denver', 'Lansing', 'Boston', 'Tallahassee', 'Austin', 'Oklahoma City', 'Honolulu', 'Juneau', 'Salt Lake City', 'Santa Fe', 'Bismarck', 'Pierre', 'Charleston', 'Richmond', 'Trenton', 'Saint Paul', 'Springfield', 'Indianapolis', 'Frankfort', 'Nashville', 'Atlanta', 'Montgomery', 'Jackson', 'Raleigh', 'Columbia', 'Augusta', 'Montpelier', 'Concord', 'Hartford', 'Providence', 'Cheyenne', 'Helena', 'Topeka', 'Des Moines', 'Harrisburg', 'Annapolis', 'Jefferson City', 'Phoenix', 'Carson City', 'Albany', 'Madison', 'Dover', 'Boise', 'Little Rock', 'Baton Rouge']

for state in states:
    print("The next state is", state)


for i in range(len(states)):
    print(f"The capital of {states[i]:10s} is {capitals[i]:10s}" )

print("The action is", end='')
print(commands[0])


print(" {:5d} is the answer to the question".format(42))
print(" { } is the answer to the question".format(42))

longest_name =''
for name in names:
    if len(name) > len(longest_name):
        longest_name = name
    else:
        if len(name)==len(longest_name) and name > longest_name:
            longest_name = name
print(longest_name)