def characterReplacement(s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    l = r = 0
    count = {}
    ret = 0
    size = len(s)
    while r<size:# and r-l+1-count[max(count)]:
        if s[r] not in count:
            count[s[r]] = 1
        else:
            count[s[r]]+=1
        while (r-l+1-max(count.values())>k):
            count[s[l]]-=1
            l+=1
        ret = max(ret, r-l+1)
        r+=1
    
    return ret