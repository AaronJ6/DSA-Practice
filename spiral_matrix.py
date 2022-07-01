def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    ret = []

    beg_row = 0
    beg_col = 0

    n = len(matrix)
    m = len(matrix[0])

    end_row = n - 1
    end_col = m - 1

    while len(ret)<(n*m):
        for i in range(beg_col, end_col+1): #going right
            ret.append(matrix[beg_row][i])
        beg_row+=1

        for i in range(beg_row, end_row+1): #going down
            ret.append(matrix[i][end_col])
        end_col-=1

        if beg_row<=end_row:
            for i in range(end_col, beg_col-1, -1): #going left
                ret.append(matrix[end_row][i])
            end_row-=1

        if beg_col<=end_col:
            for i in range(end_row, beg_row-1, -1): #going up
                ret.append(matrix[i][beg_col])
            beg_col+=1

    return ret