""" tuple = [1,2,3,4,5]

print(tuple[1:3])
tuple[1:3] = [0]
print(tuple) """

matrix = [[1,5,9],[10,11,13],[12,13,15]]

# arr = [y for x in matrix for y in x]
arr = []
for i in matrix:
    for j in i:
        arr.append(j)

print(arr)