from tempfile import tempdir


def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    if len(height) == 2: #!BRUTE FORCE
        return(min(height[0],height[1]))

    area = 0

    for l in range(len(height)):
        for r in range(l+1,len(height)):
            temp = (r-l)*(min(height[l],height[r]))
            area = max(area,temp)
    
    return(area)



height = [2,3,4,5,18,17,6]
print(maxArea(height))