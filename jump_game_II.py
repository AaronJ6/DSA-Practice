def rec(i, nums): #!My wrong recursive function
    if nums[i] != 0 and (nums[i]+i) >= (len(nums) - 1): 
        return 1
    else:
        op = 1
        if i < len(nums) and nums[i] != 0:
            i+=nums[i]
        else:
            return op
        op += rec(i, nums)
    return(op)

def func(nums):#!My wrong solution function
    ret = 0
    mn = 10000000
    for n in nums:
        for i in range(n):
            ret += rec(i,nums) 
            mn = min(ret,mn)
    return(ret)

def jump(nums): #!NEETCODE solution
    """
    :type nums: List[int]
    :rtype: int
    """
    op = 0
    l = r = 0
    
    while r < len(nums) - 1:
        farthest = 0
        for i in range(l, r+1):
            farthest = max(farthest, i + nums[i])
        l = r+1
        r = farthest
        op += 1
    return(op)
            

nums = [0,0,0,0]
op = func(nums)
# if op > 0: return True
# else: return False
print(op)