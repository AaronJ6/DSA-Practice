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
    