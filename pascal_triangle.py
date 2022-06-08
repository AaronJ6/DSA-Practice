def generate(numRows):
    op = [[1]]
    
    for i in range(1,numRows):
        prev = [0,*op[i-1],0]
        row = []
        for j in range(1,len(prev)):
            row.append(prev[j-1]+prev[j])
        op.append(row)
        
    return op 

print(generate(3))