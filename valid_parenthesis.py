def isValid(self, s):
    """
    :type s: str
    :rtype: bool
    """
    stk = []
    i = 0
    while i<len(s) and len(stk)>0:
        if s[i] == '(' or s[i] == '[' or s[i] == '{':
            stk.append(s[i])
            i+=1
        else:
            chk = stk.pop()
            if s[i] == ')' and chk != '(':
                return False
            elif s[i] == ']' and chk != '[':
                return False
            if s[i] == '}' and chk != '{':
                return False
            i+=1
    if len(stk)>0:
        return False
    else:
        return True

s = '(]'
ck = isValid(s)
print(ck)