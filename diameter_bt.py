def diameterOfBinaryTree(root):
    """
    :type root: TreeNode
    :rtype: int
    """       
    ans = 0
    
    def depth_calc(node):
        if node == None:
            return 0
        l = depth_calc(node.left)
        r = depth_calc(node.right)
        ans = max(ans,l+r)
        return 1+max(l,r)
    
    depth_calc(root)        
    return ans    
"""     left, right = root.left, root.right
    
    def depth_calc(node):
        if node == None:
            return 0
        l,r = 1, 1
        l += depth_calc(node.left) #!wouldnt check sum of path in subtrees
        r += depth_calc(node.right)
        
        return max(l,r)
    
    l_dep, r_dep = depth_calc(root.left), depth_calc(root.right)
    print(l_dep, r_dep)
    
    return (l_dep + r_dep) """
