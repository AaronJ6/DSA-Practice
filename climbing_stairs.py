def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    one, two = 1,1  #!FIBONACCI PROBLEM is the fastest way to solve this
    for i in range(n-1):
        temp = one
        one = one + two
        two = temp
    return one
"""  res = 0 #!USING HASHING
    hsh = {}
    def recur_fn(i):
        if i==n:
            return 1
        elif i>n:
            return 0
        else:
            op = 0
            if i+1 not in hsh:
                hsh[i+1] = recur_fn(i+1)
            if i+2 not in hsh:
                hsh[i+2] = recur_fn(i+2)
            op += hsh[i+1] + hsh[i+2]
            return op
    res = recur_fn(0)
    return res """

n = 5
op = climbStairs(n)
print(op)