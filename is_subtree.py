def isSameTree(self, p, q): #!RECURSION CODE
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
    
    return(self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right))