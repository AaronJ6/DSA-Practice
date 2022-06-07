def isSubsequence(s: str, t: str) -> bool:
    i = 0 #!MY CODE
    j = 0
    
    dp = [[-1]*len(t) for i in range(len(s))]
    # print(dp)
    def chk_fn(i,j):
        if(i<0 or j<0):
            return 0
        elif(dp[j][i] != -1):
            return dp[j][i]
        elif(s[j] == t[i]):
            dp[j][i] = 1 + chk_fn(i-1, j-1)
            return dp[j][i]
        else:
            dp[j][i] = chk_fn(i-1,j)
            return dp[j][i]
    
    if(chk_fn(len(t)-1,len(s)-1) == len(s)):
        return True
    else:
        return False
    """ i = 0 #!FASTEST CODE
    j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s) """
s = "axc"
t = "ahbgdc"
print(isSubsequence(s,t))