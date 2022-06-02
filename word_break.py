def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """
    i=len(s) - 1
    dp = [False]*(len(s)+1)
    dp[len(s)] = True
    for i in range(len(s)-1, -1, -1):
        for wrd in wordDict:
            l = len(wrd)
            if i+l <= len(s) and s[i:i+l] == wrd:
                dp[i] = dp[i+l]
            if dp[i]:
                break
    return dp[0]
