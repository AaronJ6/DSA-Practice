def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # sz = 0
    dp = [0]*(len(nums)-1)
    dp[0] = 1
    i = 1
    for n in nums[1:]:
        if n>nums[i-1]:
            dp[i] = 1+dp[i-1]
        else:
            # if i-2>=0 and n>nums[i-2]:
            #     dp[i] = dp[i-2]
            # else:
            dp[i] = dp[i-1]
        i+=1
    return dp[-1]

nums = [0,1,0,3,2,3]
print(lengthOfLIS(nums))