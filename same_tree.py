from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q): #! MY CODE
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        if p is None:
            return False
        if q is None:
            return False
        
        Q1 = deque([p])
        Q2 = deque([q])
        chk = 0
        
        while Q1 and Q2:
            l1 = Q1.popleft()
            l2 = Q2.popleft()
            
            if l1 and l2:
                if l1.val == l2.val:
                    Q1.append(l1.left)
                    Q1.append(l1.right)
                    Q2.append(l2.left)
                    Q2.append(l2.right)
                else:
                    chk = 1
                    break
            elif l1 or l2:
                chk = 1
                break
        if chk == 1:
            return False
        else:
            return True

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