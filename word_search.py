def exist(board, word): #!NEETCODE/MY CODE
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """
    #* O(n*m*4*len(word)) - 4*len(word) cuz we call the rec fn 4 times
    m = len(board)
    n = len(board[0])
    
    wrd = len(word)
    path = set()
    
    def rec_fn(i,j,l_wrd):
        if l_wrd == wrd:
            return True
        if (i<0 or j<0 or i>=m or j>=n or word[l_wrd]!=board[i][j] or (i,j) in path):
            return False
        
        path.add((i,j))
        op1 = rec_fn(i-1,j,l_wrd+1)
        op2 = rec_fn(i+1,j,l_wrd+1)
        op3 = rec_fn(i,j-1,l_wrd+1)
        op4 = rec_fn(i,j+1,l_wrd+1)
        path.remove((i,j))
        
        return op1 or op2 or op3 or op4
    
    for l in range(m):
        for k in range(n):
            if rec_fn(l,k,0):
                return True
    
    return False