def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    stk = []
    closed_bracket = {')':'(', ']':'[', '}':'{'}
    for i in s:
        if i in closed_bracket:
            if stk and stk[-1] == closed_bracket[i]:
                stk.pop()
            else:
                return False
    if not stk:
        return True
    else:
        return False

s = '(){}}{'
ck = isValid(s)
print(ck)