def lengthOfLongestSubstring(s): #!NEETCODE
    """
    :type s: str
    :rtype: int
    """
    l = 0
    mx = 0
    
    l_wrd = len(s)
    chk={}
    
    for r in range(len(s)):
        if s[r] not in chk:
            mx = max(mx, r-l+1)
        else:
            if chk[s[r]]<l:
                mx = max(mx, r-l+1)
            else:
                l = chk[s[r]]+1
        chk[s[r]] = r
    
    return mx

"""
indext    0    1    2    3   4   5   6   7
string    a    c    b    d   b   a   c   d
          ^                  ^
          |                  |
		left               right
		seen = {a : 0, c : 1, b : 2, d: 3} 
		# case 1: seen[b] = 2, current window  is s[0:4] , 
		#        b is inside current window, seen[b] = 2 > left = 0. Move left pointer to seen[b] + 1 = 3
		seen = {a : 0, c : 1, b : 4, d: 3} 
indext    0    1    2    3   4   5   6   7
string    a    c    b    d   b   a   c   d
						 ^   ^
					     |   |
				      left  right		
indext    0    1    2    3   4   5   6   7
string    a    c    b    d   b   a   c   d
					     ^       ^
					     |       |
				       left    right		
		# case 2: seen[a] = 0,which means a not in current window s[3:5] , since seen[a] = 0 < left = 3 
		# we can keep moving right pointer


    There are two cases if s[r] in seen:
    case1: s[r] is inside the current window, we need to change the window by moving left pointer to seen[s[r]] + 1.
    case2: s[r] is not inside the current window, we can keep increase the window
"""