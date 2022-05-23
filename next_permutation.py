def nextPermutation(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    idx = -1 #!Checked multiple yt vids
    prev = -1
    
    for i in range(len(nums)-2, -1, -1):
        if nums[i] < nums[i+1]:
            idx = i
            break
    if idx>=0:
        prev = idx+1
        for i in range(idx+1,len(nums)):
            if nums[i]>nums[idx] and nums[i]<nums[prev]:
                prev = i
        nums[idx], nums[prev] = nums[prev], nums[idx]
        nums[idx+1:] = sorted(nums[idx+1:])
    else:
        nums.reverse()
    