def coinChange(coins, amount): #!MY CODE - WRONG
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    r = len(coins)-1
    count = 0
    while r>=0 and amount>=0:
        temp = amount - coins[r]
        if temp<0:
            r-=1
            continue
        count+=1
        while temp>coins[r]:
            temp-=coins[r]
            count+=1
        amount=temp
        r-=1
    if count>0:
        return count
    else:
        return -1