def isPalindrome(s): #!NEETCODE
    """
    :type s: str
    :rtype: bool
    """
    def alphanum(ch):
        return(ord('A') <= ord(ch) <= ord('Z') or 
               ord('a') <= ord(ch) <= ord('z') or 
               ord('0') <= ord(ch) <= ord('9'))
    i = 0
    j = len(s) - 1
    while i<j:
        while i<j and not alphanum(s[i]):
            i+=1
        while j>i and not alphanum(s[j]):
            j-=1
        if s[i].lower() != s[j].lower():
            return False   
        i, j = i+1, j-1
    return True

    """     s = ''.join(ch for ch in s if ch.isalnum()) #! MY CODE
        i = 0
        j = len(s)-1
        while(i<=j):
            if s[i].lower() != s[j].lower():
                return False
            i+=1
            j-=1
        return True """

s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))