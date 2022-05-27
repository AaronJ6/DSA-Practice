def countAndSay(n):
    """
    :type n: int
    :rtype: str
    """
    op = ""
    count = 1
    temp = n%10
    n = n//10
    while n>0:
        chk = n%10
        if chk == temp:
            count+=1
        else:
            if count>1:
                op = str(count) + str(temp) + op
            else:
                op = str(temp) + op
            temp = chk
            count = 1
        n = n//10
    if count>1:
        op = str(count) + str(temp) + op
    else:
        op = str(temp) + op
    print(op)
    # return op

n = 4
countAndSay(n)