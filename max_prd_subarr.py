def my_maxProduct(nums): #!My wrong method...FAIL
    """
    :type nums: List[int]
    :rtype: int
    """
    mx = -999999
    currM = 1
    
    for i in range(len(nums)):
        currM*=nums[i]
        mx = max(mx, currM)
        if currM <= 0: 
            if currM == 0: 
                mx = 0
                currM = 1
                continue
            elif i+1 < len(nums):
                if nums[i+1] < 0:
                    continue
            currM = 1
    return(mx)

def maxProduct(nums): #!NEETCODE
    """
    :type nums: List[int]
    :rtype: int
    """
    op = max(nums)
    currMax = 1
    currMin = 1
    
    for n in nums:
        if n == 0:
            currMax = 1
            currMin = 1
            continue
        tmp = currMax * n
        currMax = max(tmp, currMin*n, n) #comparing it to n is a very imp point
        currMin = min(tmp, currMin*n, n)
        
        op = max(op,currMax, currMin)
            
    return(op)

def main():
    nums = [-3,-1,-1]
    op = maxProduct(nums)
    print(op)

if __name__ == "__main__":
    main()