def numDecodings(s): #!NEETCODE
    """
    :type s: str
    :rtype: int
    """
    dp = {len(s) : 1}
    
    def dfs(i):
        if i in dp:
            return dp[i]
        if s[i] == "0":
            return 0
        res = dfs(i+1)
        if i+1<len(s) and (s[i] == '1' or (s[i] == '2' and s[i+1] in "0123456")):
            res+=dfs(i+2)
        dp[i] = res
        return res
    return dfs(0)

def rec_fn(i, s):
    if i >= len(s):
        return 0
    else:
        lng1, lng2 = 1, 1 #!BRUTE FORCE
        num1 = int(s[i])
        if i+1<len(s):
            num2 = int(s[i])
            num2 = num2*10 + int(s[i+1])
        else:
            num2 = 0
        if num1>0 and num1<27:
            lng1 += rec_fn(i+1,s)
        else:
            lng1 = -1
        if num2>0 and num2<27:
            lng2 += rec_fn(i+2,s)
        else:
            lng2 = -1
        return max(lng1, lng2)

s = "106"
print(numDecodings(s))