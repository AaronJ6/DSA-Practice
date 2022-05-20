def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    """
    #? The below solution maybe faster, but it depends on the 
    #? in-built sort function, where the time and space complexity 
    #? could be more than expected. Sometimes interviewers take space
    #? as O(1) for in-built. So better to write own sorting algo and work it.
    return(sorted(s) == sorted(t)) #!NEETCODE #1 """
        
    if(len(s) != len(t)): #! NEETCODE #2
        return False
    
    #! return(Counter(s) == Counter(t)) 
    #? The whole code below can be done in one line,
    #? which is written above.

    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    for c in countS:
        if countS[c] != countT.get(c, 0):
            return False
    return True
    

    """ if(len(s) != len(t)): #! MY CODE
        return False
    for post in range(len(t)):
        if t[post] not in s:
            return False
        s = s.replace('t[post]', '')
    return True  """

s = 'ccac'
t = 'aacc'
if isAnagram(t,s):
    print("TRUE")
else:
    print("FALSE")