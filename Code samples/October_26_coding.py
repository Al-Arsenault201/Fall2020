RANK = 0
GOLDS = 1
SILVERS = 2
BRONZES = 3
TOTAL = 4

medal_table = [
   [1, 14, 11,4,29],
   [2,5,2,4,11],
   [3,3,5,4,12],
   [4,3,3,3,9],
   [5,2,5,1,8],
   [6,2,3,0,5],
   [7,2,0,4,6],
]
for i in range(len(medal_table)):
    print(medal_table[i][-1])

for i in range(len(medal_table)):
    print(medal_table[i][TOTAL])

golds_won = 0
for i in range(len(medal_table)):
   golds_won += medal_table[i][GOLDS]
print(golds_won)


ROWS = 5
COLUMNS = 10
square_table = []  #create the initial blank table
num_to_be_squared = 1
for i in range(ROWS):
   row = []
   for j in range(COLUMNS):
       row.append(num_to_be_squared**2)
       num_to_be_squared += 1
   square_table.append(row)
   print(row)
print(square_table)

countries =["United States", "Kenya", "Jamaica", "China", "Ethiopia", "Great Britain", "Germany"]
for i in range(len(medal_table)):
   medal_table[i].insert(1, countries[i])


for k in range(len(medal_table)):
   print(medal_table[k])

RANK = 0
COUNTRY = 1
GOLDS = 2
SILVERS = 3
BRONZES = 4
TOTALS = 5
golds_won = 0
for i in range(len(medal_table)):
   golds_won += medal_table[i][GOLDS]
print(golds_won)
