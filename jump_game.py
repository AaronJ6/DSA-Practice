def canJump(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    end = len(nums) - 1
    
    for i in range(len(nums)-1, -1, -1):
        if(i+nums[i]>=end):
            end = i
    return True if end == 0 else False    

""" We are working from the back of the array, 
    and ensuring that we reach the beginning of the array 
    from the end, if it doesnt happen 
    (that means it can either end at some point in the middle 
    of the array or went beyond 0 which shouldnt be possible ig)
    The check we do - if the sum of current position + the number 
    in that position can reach the position which we just passed by. """