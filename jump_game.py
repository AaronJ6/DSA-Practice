def rec(i, nums):
    if i == (len(nums) - 1): 
        return 1
    else:
        op = 0
        if i < len(nums) and i != 0:
            i+=nums[i]
        elif i == 0: i += 1
        else:
            return op
        op += rec(i, nums)
    return(op)

def func(nums):
    ret = 0
    for i in range(len(nums)):
        ret += rec(i,nums) 
    return(ret) 

nums = [0,0,0,0]
op = func(nums)
# if op > 0: return True
# else: return False
print(op)