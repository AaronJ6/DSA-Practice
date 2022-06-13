def canFinish(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """
    if len(prerequisites) == 0:
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
    
    return possible

numC = 3
prereq = [[0,2],[1,2],[2,0]]
print(canFinish(numC, prereq))