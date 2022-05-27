def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: bool
    """
   
    l = 0
    r = len(nums)-1
    trav = []
    while(l<=r):
        if nums[l] == target or nums[r] == target:
            return True
        mid = (l+r)//2
        if nums[mid]==target:
            return True
        if target>=nums[l] and target<nums[mid]:
                r = mid - 1
        if target<=nums[r] and target>nums[mid]:
                l = mid + 1
        else:
            l+=1
            r-=1
    return False

nums = [1,0,1,1,1]
print(search(nums,0))
            
        