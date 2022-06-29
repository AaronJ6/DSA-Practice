def countHousePlacements(n): 
    #* Similar to a fibonacci series, 
    #* where the n values is updated using sum of prev 2 vals
    if(n==1):return 4
    if(n==2):return 9
    
    MOD=pow(10,9)+7
    
    prev_prev=2
    prev=3
    for i in range(3,n+1):
        current=prev+prev_prev
        prev_prev=prev
        prev=current
        
    return (prev*prev)%MOD

# def countHousePlacements(self, n): #*MY code using the logic of final steps problem
#     """
#     :type n: int
#     :rtype: int
#     """
#     dp = [0]*(n+1)
#     dp[0] = 1
#     dp[1] = 2
#     for j in range(2,n+1):
#         dp[j] = dp[j-1] + dp[j-2]
    
#     MOD=pow(10,9)+7
    
#     ret = (dp[n]*dp[n]) % MOD
    
#     return ret