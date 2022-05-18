def rob(nums): #!NEETCODE
    """
    :type nums: List[int]
    :rtype: int
    """
    sum1, sum2 = 0, 0
    
    for n in nums:
        temp = max(n+sum1, sum2)
        sum1 = sum2
        sum2 = temp
    return sum2

"""     
#!FASTEST CODE ON LEETCODE - whats the difference from working this problem 
#! from the back and front, but back is faster
    robOption1 = 0 
    robOption2 = 0
    #print(range(len(nums)-1, -1, -1))
    for money in range(len(nums)-1, -1, -1):
        oldRobOption1 = robOption1
        robOption1 = max(robOption1, nums[money] + robOption2)
        robOption2 = max(oldRobOption1, robOption2)
        
    return robOption1 """
    