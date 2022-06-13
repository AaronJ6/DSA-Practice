def pacificAtlantic(heights):
    """
    :type heights: List[List[int]]
    :rtype: List[List[int]]
    """
    row, col = len(heights), len(heights[0])    
    pac, atl = set(), set()
    
    def dfs(r,c,visit,prevH):
        if ( (r,c) in visit or r<0 or c<0 or r==row or c==col or heights[r][c]<prevH):
            return
        visit.add((r,c))
        dfs(r+1,c,visit,heights[r][c])
        dfs(r-1,c,visit,heights[r][c])
        dfs(r,c+1,visit,heights[r][c])
        dfs(r,c-1,visit,heights[r][c])
        
        
    for c in range(col):
        dfs(0,c,pac,heights[0][c])
        dfs(row-1,c,atl,heights[row-1][c])
    
    for r in range(row):
        dfs(r,0,pac,heights[r][0])
        dfs(r,col-1,atl,heights[r][col-1])
        
    res = list(pac.intersection(atl))
    return res

heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
pacificAtlantic(heights)