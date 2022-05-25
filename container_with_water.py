def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    if len(height) == 2:
        return(height[0]*height[1])
    
    breadth = 1
    i, j = 1, 0
    area = 0

    while i<len(height):
        ht = min(height[0], height[i])
        temp = ht*breadth
        area = max(area,temp)
        i+=1
        breadth+=1
    breadth-=1
    while j<i:
        ht = min(height[j], height[i-1])
        temp = ht*breadth
        area = max(area,temp)
        j+=1
        breadth-=1
    return(area)