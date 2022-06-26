def maximumXOR(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    mx = 0
    for i in nums:
        mx = mx | i
    
    return mx

# nums[i] = nums[i] AND (nums[i] XOR x) where x is ANY integer, basically means you can decrease that element into any number but can't increase it.
# Reread the above statement. That's the key to solving the problem!

# AND operation can only allow a 1 to be 0 but not a 0 to become 1.
# XOR of elements is maximised by getting distinct combination of a 0 and 1.
# So bascially in the answer you get a 0 where all numbers in array have the bit place values 0, as there is no way to make it into a 1 .
# Rest can be made into a 1, as atleast one number in the array has a bit place value 1.
# And obviously you can check if atleast one of the element has a place value 1 by doing a cumulative OR.