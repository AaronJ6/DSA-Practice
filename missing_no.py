def missingNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # op = 0 #!MY SOLN
    # for i in range(len(nums)+1):
    #     if i not in nums:
    #         op = i
    #         break
    # return op

    op = len(nums) #!NEETCODE Method 2 in another way without gauss SUM
    for i in range(len(nums)):
        op += (i-nums[i])
    return op
  
    # op = len(nums) #! NEETCODE XOR SOLN
    # for i in range(len(nums)):
    #     op = op^i^nums[i]
    # return(op)

    """ gsum = (len(nums) *(len(nums)+1))//2 #!NEETCODE Method 2
    nsum = sum(nums)
    return(gsum - nsum) """

nums = [3,0,1]
op = missingNumber(nums)
print(op)
        