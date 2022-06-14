import collections

def numIslands_bfs(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    if not grid:
        return
    
    ROWS, COLS = len(grid), len(grid[0])
    visit = set()
    islands = 0
    
    def bfs(r,c,visit):
        q = collections.deque()
        visit.add((r,c))
        q.append((r,c))
        while q:
            row, col = q.popleft()
            directions = [[1,0], [0,1], [-1,0], [0,-1]]
            
            for dr, dc in directions:
                r, c = row+dr, col+dc
                if ( (r,c) not in visit and r in range(ROWS) and c in 
                    range(COLS) and grid[r][c]=="1"):
                    q.append((r,c))
                    visit.add((r,c))
        
        
    
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == "1" and (r,c) not in visit:
                bfs(r,c,visit)
                islands+=1
    return islands

def numIslands_dfs(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    def part(i, j, grid):
        if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j]!= '1':
            return
        else:
            grid[i][j] = '0'
        part(i, j+1, grid)
        part(i,j-1,grid)
        part(i+1, j, grid)
        part(i-1,j,grid)
    def islands(grid):
        iss = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    iss += 1
                    part(i,j,grid)
        return iss
    return islands(grid)