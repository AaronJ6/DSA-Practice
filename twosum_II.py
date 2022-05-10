def twoSum_II(self, numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    l = 0
    r = len(numbers)-1
    op = set()
    while(l<r):
        chk = numbers[l] + numbers[r]
        if(chk<target): l+=1
        elif(chk>target): r-=1
        else:
            op.add(l+1)
            op.add(r+1)
            break
    return(op)