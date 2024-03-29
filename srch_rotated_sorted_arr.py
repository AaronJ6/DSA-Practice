def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    l = 0 #! NEETCODE
    r = len(nums)-1
    while(l<=r):
        mid = (l+r)//2
        if(nums[mid] == target):
            return mid
        if nums[l]<nums[mid]:
            if target<nums[mid] or target<nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        else:
            if target<nums[mid] or target > nums[r]:
                r = mid - 1
            else:
                l = mid + 1
    return -1

nums = [4,5,6,7,0,1,2]
target = 2
op = search(nums, target)
print(op)