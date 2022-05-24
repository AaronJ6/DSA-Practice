def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    op = -1
    
    l = 0
    r = len(nums)-1
    while(l<=r):
        mid = l+r//2
        if(nums[mid] == target):
            op = mid
        if nums[mid]>nums[l]:
            if target<nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        else:
            if target > nums[l]:
                r = mid - 1
            else:
                l = mid + 1
    return op