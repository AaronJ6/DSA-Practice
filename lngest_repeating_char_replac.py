def characterReplacement(s, k): #!O(26*n) - Time complexity
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

def characterReplacement(s, k): #!O(n) because we have a 'maxf' var to store the largest 
    #! freq in the dictionary and even if the val decreases the need to update the maxf 
    #! isnt necessary cuz we change res only when maxf increases
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    l = r = 0
    count = {}
    ret = 0
    maxf = 0
    size = len(s)
    while r<size:
        count[s[r]] = 1 + count.get(s[r],0)
        maxf = max(maxf, count[s[r]])
        while (r-l+1-maxf>k):
            count[s[l]]-=1
            l+=1
        ret = max(ret, r-l+1)
        r+=1
    
    return ret