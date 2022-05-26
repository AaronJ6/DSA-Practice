def lowestCommonAncestor(root, p, q): #*Assuming that the node is sure to find, if not assuming
                                        #* We use a stack to compare the common ancestor - but takes a lot of space
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    if not root:
        return None
    elif root.val == p.val or root.val == q.val:
        return root
    b = lowestCommonAncestor(root.left, p, q)
    c = lowestCommonAncestor(root.right, p, q)
    
    if not b:
        return c
    elif not c:
        return b
    else:
        return root