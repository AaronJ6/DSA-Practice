def canFinish(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """
    if prerequisites is None:
        return True
    check = {}
    possible = False
    
    def chk_fn(pre):
        check[pre[1]] = pre[0]
        if pre[1] in check:
            if pre[0] in check and check[pre[0]] == pre[1]:
                return False
            else:
                return True                
            
    for prerq in prerequisites:
        possible = chk_fn(prerq)
    
    return possible