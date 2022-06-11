def uniquePaths(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    dp = [[0 for i in range(n)] for j in range(m)] #!MY CODE WITH REC+MEMOIZATION
    dp[m-1][n-1] = 1
    # print(path)
    def rec_fn(i,j):
        if i<m and j<n:
            if dp[i][j] > 0:
                return dp[i][j]
            if i==m-1 and j==n-1:
                return 1

            dp[i][j]+=rec_fn(i,j+1)
            dp[i][j]+=rec_fn(i+1,j)
            return dp[i][j]
        else:
            return 0
    
    return rec_fn(0,0)

def uniquePaths(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    row = [1]*n #*bottom row initialised as 1
    
    for i in range(m-1):#*going through all rows except the last
        newRow = [1]*n #*the current row
        for j in range(n-2, -1, -1): #*n-2 because the last column is always 1
            newRow[j] = newRow[j+1] + row[j]  #*newRow[j+1] is the for taking the val from next column and row is for the row below it
        row = newRow #*that is why we update row with newRow since we want row to be having the vals of the row below current(newRow)
    
    return row[0]
        