def uniquePaths(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    dp = [[0 for i in range(n)] for j in range(m)]
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
        