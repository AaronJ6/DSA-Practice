def rob(nums): #!MY CODE
    """
    :type nums: List[int]
    :rtype: int
    """

    if len(nums) == 0:
        return
    elif len(nums) == 1:
        return nums[0]
    elif len(nums) == 2:
        return max(nums[0], nums[1])
    else:
        return max(rob_fn(nums, 1, len(nums)), rob_fn(nums, 0, len(nums)-1))

def rob_fn(nums, start, end):
    sum1, sum2 = 0, 0
    for i in range(start, end):
        temp = max(nums[i]+sum1, sum2)
        sum1 = sum2
        sum2 = temp
    return sum2