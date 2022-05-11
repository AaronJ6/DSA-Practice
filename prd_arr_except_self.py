def productExceptSelf(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    op = [1]*len(nums)#[1]
    j = len(nums)-1
    post = 1
    pre = 1
    for i in range(len(nums)):
        op[i] = pre
        pre *= nums[i]
        #op.append(op[i-1]*nums[i-1]) #!MY METHOD
    while j>=0:
        op[j] = op[j] * post
        post = post * nums[j]
        j-=1
    return op