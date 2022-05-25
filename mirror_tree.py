from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mirrorTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        
        return(self.mirrorTree(p.left,q.right) and self.mirrorTree(p.right,q.left))

    def isSameTree(self, p): #!RECURSION CODE
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        print(self.mirrorTree(p.left,p.right))