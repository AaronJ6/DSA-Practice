import collections

def numIslands(grid):
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