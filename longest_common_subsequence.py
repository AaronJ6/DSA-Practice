def longestCommonSubsequence(text1, text2):
    """
    :type text1: str
    :type text2: str
    :rtype: int
    """
    #!NEETCODE - 2D DP - bottom up problem

    dp = [[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]

    for i in range(len(text1)-1, -1, -1):
        for j in range(len(text2)-1, -1, -1):
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dp[i+1][j+1]
            else:
                dp[i][j] = max(dp[i][j+1], dp[i+1][j])

    return dp[0][0]

"""     check = "" #!MY CODE - Wrong
    num = 0
    j=0
    for i in range(len(text1)):
        if text1[i] in text2[j:]:
            check+=text1[i]
            j = text2.index(text1[i])+1

    # if check == text2:
    num = len(check)
    return num """

text1 = "abcde"
text2 = "ace"
print(longestCommonSubsequence(text1,text2))