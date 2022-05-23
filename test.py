nums = [2,3,3,1,3]
i = 2
print(nums)
nums[i+1:] = nums[i+1:][::-1]
print(nums)