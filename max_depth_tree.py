# Definition for a binary tree node.
from collections import deque #!Queue DS from libararies


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        op = self.depth(root)
        return op
        
    def depth(self, temp): #!MY CODE
        if temp == None:
            return 0
        else:
            opl, opr = 1, 1
            opl += self.depth(temp.left)
            opr += self.depth(temp.right)
            return(max(opl,opr))  

    def maxDepth(self, root): #! NEETCODE Iterative BFS
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        q = deque([root])
        level = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level+=1
        return(level)