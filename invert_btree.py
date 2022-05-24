from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def invertTree(self, root): #! MY CODE
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        
        q = deque([root])
        while q:
            node = q.popleft()
            if node:
                if node.left and node.right:
                    node.left, node.right = node.right, node.left
                    q.append(node.left)
                    q.append(node.right)
                elif node.left:
                    node.right = node.left
                    node.left = None
                    q.append(node.right)
                elif node.right:
                    node.left = node.right
                    node.right = None
                    q.append(node.left)
        return root

    def invertTree(self, root): #! Recursive fastest code
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return root
        else:
            temp = root.left
            root.left = root.right
            root.right = temp
            self.invertTree(root.right)
            self.invertTree(root.left)
        return root