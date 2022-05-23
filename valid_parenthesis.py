def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    stk = []
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '[' or s[i] == '{':
            stk.append(s[i])
        else:
            chk = stk.pop()
            if s[i] != chk:
                return False
    return True

s = '()'
ck = isValid(s)
print(ck)