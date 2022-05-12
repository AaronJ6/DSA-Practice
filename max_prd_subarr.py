def maxProduct(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    mx = -999999
    currM = 1
    
    for n in nums:
        currM*=n
        if currM <= 0: 
            if currM == 0: 
                mx = 0
                currM = 1
                continue
            currM = 1
        mx = max(mx, currM)
    return(mx)