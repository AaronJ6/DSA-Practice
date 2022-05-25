def threeSum(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    op = []
    nums.sort()
    
    for i, a in enumerate(nums):
        if i>0 and (a == nums[i-1]):
            continue

        l = i+1
        r = len(nums)-1
        
        while(l<r):
            temp = nums[i]
            temp += nums[l] + nums[r]
            if temp>0:
                r-=1
            elif temp<0:
                l+=1
            else:
                op.append([nums[i],nums[l],nums[r]])
                l+=1
                while nums[l] == nums[l-1] and l<r:
                    l+=1
    return op                   