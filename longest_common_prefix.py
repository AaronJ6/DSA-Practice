def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if strs==None or len(strs)==0:
        return ""
    return commonPrefix(strs, 0, len(strs)-1)

def commonPrefix(strs, l, r):
    if l==r:
        return strs[l]
    else:
        mid = (l+r)//2
        l_sub = commonPrefix(strs, l, mid)
        r_sub = commonPrefix(strs, mid+1, r)
        
        return checkPrefix(l_sub, r_sub)

def checkPrefix (lsub, rsub):
    mn = min(len(lsub), len(rsub))
    for i in range(mn):
        if lsub[i] != rsub[i]:
            return lsub[0:i]
    return lsub[0:mn]