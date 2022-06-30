def setZeroes(matrix): #* MY Code
    #! Space complexity = O(m+n)
    #! Time = O(m*n)
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    s_row = len(matrix)
    s_col = len(matrix[0])
    
    row = set()
    col = set()
    
    for i in range(s_row):
        for j in range(s_col):
            if matrix[i][j] == 0:
                row.add(i)
                col.add(j)
    
    for i in row:
        for j in range(s_col):
            matrix[i][j] = 0
    for i in col:
        for j in range(s_row):
            matrix[j][i] = 0

#!NEETCODE - O(1) Space complexity
            #!O(m+n) Time complexity
def setZeroes(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    rowZero = False
    s_row = len(matrix)
    s_col = len(matrix[0])
    
    for r in range(s_row):
        for c in range(s_col):
            if matrix[r][c] == 0:
                matrix[0][c] = 0
                if r>0:
                    matrix[r][0] = 0
                else:
                    rowZero = True
    
    for r in range(1,s_row):
        for c in range(1,s_col):
            if matrix[0][c]==0 or matrix[r][0]==0:
                matrix[r][c] = 0
    
    if matrix[0][0] == 0:
        for r in range(s_row):
            matrix[r][0] = 0
    
    if rowZero:
        for c in range(s_col):
            matrix[0][c] = 0
                
    