def lengthOfLIS(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    sz = 0
    dp = [0]*len(nums)
    dp[0] = 1
    for i,n in enumerate(nums[1:]):
        if n>nums[i-1]:
            dp[i] = 1+dp[i-1]
        else:
            if i-2>=0 and n>nums[i-2]:
                dp[i] = dp[i-2]
            else:
                dp[i] = dp[i-1]
    return dp[-1]