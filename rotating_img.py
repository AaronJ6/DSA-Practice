def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    temp = 0
    l = 0
    r = len(matrix[0])-1
    
    #O(n^2) - time complexity
    while l<r:
        top, bottom = l,r
        for i in range(r-l):
            topLeft = matrix[top][l+i] #saving no. of top left
            
            #move bottom left to top left
            matrix[top][l+i] = matrix[bottom-i][l]
            
            #move bottom right to bottom left
            matrix[bottom-i][l] = matrix[bottom][r-i]
            
            #move top right to bottom right
            matrix[bottom][r-i] = matrix[top+i][r]
            
            #move top left to top right
            matrix[top+i][r] = topLeft
        r-=1
        l+=1