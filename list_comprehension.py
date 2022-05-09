matrix = [[1,5,9],[10,11,13],[12,13,15]]

# arr = [y for x in matrix for y in x] #!all the elements of a matrix made into one list
arr = []
for i in matrix:
    for j in i:
        arr.append(j)

print(arr)

arr = [[row[i] for row in matrix] for i in range(3)] #! make the rows into a column
""" for i in range(3):
     transposed_row = []
     for row in matrix:
            transposed_row.append(row[i])
     transposed.append(transposed_row) """
print(arr)

arr = [[0 for col in range(4)] for row in range(3)] #! make a matrix [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
""" for x in range(3):
    nested = []
    matrix.append(nested)
    for row in range(4):
        nested.append(0) """

print(arr)
