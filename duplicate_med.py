def findDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    hash = [0]*len(nums)
    for i in nums:
        if hash[i]>0:
            return i
        hash[i]+=1;
    