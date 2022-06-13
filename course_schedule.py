def canFinish(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """
    preMap = { i:[] for i in range(numCourses)}
    visit = set()
    
    for pre in prerequisites:
        preMap[pre[1]].append(pre[0])
    
    def dfs(node):
        if node in visit:
            return False
        if preMap[node] == []:
            return True
        
        visit.add(node)
        for pre in preMap[node]:
            if not dfs(pre):
                return False
        visit.remove(node)
        preMap[node] = []
        return True
    for crs in range(numCourses):
        if not dfs(crs): return False
    
    return True
    
"""     if len(prerequisites) == 0:
        return True
    check = {}
    possible = True

    def chk_fn(pre):
        if pre[1] == pre[0]:
            return False
        check[pre[1]] = pre[0]
        if pre[1] in check:
            if pre[0] in check and check[pre[0]] == pre[1]:
                return False
            else:
                return True                
            
    for prerq in prerequisites:
        possible = (possible and chk_fn(prerq))
    
    return possible """
numC = 3
prereq = [[0,2],[1,2],[2,0]]
print(canFinish(numC, prereq))