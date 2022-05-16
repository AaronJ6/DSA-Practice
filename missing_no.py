def missingNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    op = 0
    for i in range(len(nums)+1):
        if i not in nums:
            op = i
            break
    return op
        