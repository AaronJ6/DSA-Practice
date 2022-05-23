def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    stk = []
    if(len(s)<2):
        return False
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '[' or s[i] == '{':
            stk.append(s[i])
        else:
            chk = stk.pop()
            if s[i] == ')' and chk != '(':
                return False
            elif s[i] == ']' and chk != '[':
                return False
            if s[i] == '}' and chk != '{':
                return False
    return True

s = '(]'
ck = isValid(s)
print(ck)