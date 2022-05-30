def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # sz = 0
    dp = [0]*len(nums)
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

nums = [10,9,2,5,3,7,101,18]
print(lengthOfLIS(nums))