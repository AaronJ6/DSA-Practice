def find_island(m, n, i, j, grid):
    if (i+1 <= (m-1)):
        if (grid[i+1][j]=='1'):
            grid[i+1][j] = '2'
            find_island(m,n,i+1,j,grid)
    if (j+1 <= (n-1)):
        if (grid[i][j+1]=='1'):
            grid[i][j+1] = '2'
            find_island(m,n,i,j+1,grid)
    if (i-1 >= 0):
        if (grid[i-1][j]=='1'):
            grid[i-1][j] = '2'
            find_island(m,n,i-1,j,grid)
    if (j-1 >= 0):
        if (grid[i][j-1]=='1'):
            grid[i][j-1] = '2'
            find_island(m,n,i,j-1,grid)



def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    number_of_islands = 0;
    i = 0;
    j = 0;
    m = len(grid);
    n = len(grid[0]);
    while ((i <= m-1) or (j <= n-1)):
        if (grid[i][j]=='0' or grid[i][j]=='2'):
            if (j < n-1):
                j = j+1;
            elif ((j == (n-1)) and (i < (m-1))):
                i = i+1;
                j = 0;
            elif ((j == (n-1)) and (i == (m-1))):
                return number_of_islands
        elif (grid[i][j]=='1'):
            grid[i][j] = '2'
            find_island(m,n,i,j,grid)
            number_of_islands = number_of_islands + 1
    return number_of_islands

grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
print(numIslands(grid))