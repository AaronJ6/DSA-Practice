from pickle import FALSE
from typing import Counter


def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    """     
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
        if countS[c] != countT.get(countT[c], 0):
            return False
    return True """
    

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
    print(FALSE)