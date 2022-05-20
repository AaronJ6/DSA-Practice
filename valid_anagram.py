from pickle import FALSE


def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if(len(s) != len(t)):
        return False
    for post in range(len(t)):
        if t[post] not in s:
            return False
        s = s.replace('t[post]', '')
    return True 

s = 'ccac'
t = 'aacc'
if isAnagram(t,s):
    print("TRUE")
else:
    print(FALSE)