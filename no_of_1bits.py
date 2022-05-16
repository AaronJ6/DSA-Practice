def hammingWeight(n):
    """
    :type n: int
    :rtype: int
    """
    op = 0
    while(n != 0):
        op += 1
        n = n&(n-1)
        """
        op = n%2
        n = n//2
        #!FASTER
        """
    return op
    