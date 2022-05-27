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

def coinChange(coins, amount): #!NEETCODE
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    dp = [amount+1] * (amount+1)
    dp[0] = 0
    
    for a in range(1,amount+1):
        for c in coins:
            temp = a-c
            if temp>=0:
                dp[a] = min(dp[a],1+dp[temp])
    return dp[amount] if dp[amount]!=amount+1 else -1