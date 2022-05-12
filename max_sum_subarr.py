def maxSubArray(nums): #similar to sliding window but with just one pointer
    """
    :type nums: List[int]
    :rtype: int
    """
    curr, maxS = 0, nums[0]
    for n in nums:
        if curr < 0:
            curr = 0
        curr += n
        maxS = max(maxS, curr)
    return(maxS)