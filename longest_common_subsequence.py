def longestCommonSubsequence(text1, text2):
    """
    :type text1: str
    :type text2: str
    :rtype: int
    """
    check = ""
    num = 0
    j=0
    for i in range(len(text1)):
        if text1[i] in text2[j:]:
            check+=text1[i]
            j = text2.index(text1[i])+1

    # if check == text2:
    num = len(check)
    return num

text1 = "abcde"
text2 = "ace"
print(longestCommonSubsequence(text1,text2))