def maximumXOR(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    mx = 0
    for i in nums:
        mx = mx | i
    
    return mx