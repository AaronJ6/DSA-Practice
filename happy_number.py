def isHappy(n):
    """
    :type n: int
    :rtype: bool
    """
    loop = set()
    old = False        
    while n not in loop:
        loop.add(n)
        n = str(n)
        nums = [i for i in n]
        total = 0
        for d in nums:
            total+=(int(d)**2)
        if total == 1:
            old = True
            break
        else:
            n = total
    
    return old