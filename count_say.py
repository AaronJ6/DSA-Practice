def countAndSay(n):
    """
    :type n: int
    :rtype: str
    """
    op = ""
    count = 0
    temp = n%10
    n = n//10
    while n>0:
        chk = n%10
        if chk == temp:
            count+=1
        else:
            op = op + str(count) + str(temp)
            temp = chk
            count = 0
        n//10
    print(op)
    # return op
        
                
            