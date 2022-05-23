def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    stk = []
    i = 0
    stk.append(s[i])
    i+=1    
    while i<len(s):
        if s[i] == '(' or s[i] == '[' or s[i] == '{':
            stk.append(s[i])
            i+=1
        else:
            chk = stk.pop()
            if chk != None:
                if s[i] == ')' and chk != '(':
                    return False
                elif s[i] == ']' and chk != '[':
                    return False
                elif s[i] == '}' and chk != '{':
                    return False
            else:
                return False
            i+=1
    if len(stk)>0:
        return False
    else:
        return True

s = '(){}}{'
ck = isValid(s)
print(ck)