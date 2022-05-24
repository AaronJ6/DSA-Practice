def findMin(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    res = nums[0]    
    l = 0
    r = len(nums)-1
    mid = 0
    while l<=r:
        if nums[l]<nums[r]:
            res = min(res, nums[l])
            break
        mid = (l+r)//2
        res = min(res, nums[mid])
        if nums[mid]>nums[l]:
            l = mid + 1
        else:
            r = mid - 1
    return res