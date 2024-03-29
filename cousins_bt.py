from collections import deque
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isCousins(self, root, x, y): #!SIMPLIFIED version of the below function
        queue = deque()
        queue.append((root, 0))
        dist={}
        
        while queue:
            node,depth = queue.popleft()
            if node.left:
                dist[node.left.val] = (node.val, depth+1)
                queue.append((node.left, depth+1))
            if node.right:
                dist[node.right.val] = (node.val, depth+1)
                queue.append((node.right, depth+1))
        
        if x not in dist or y not in dist: 
            return False
        
        x_parent, x_depth = dist[x]
        y_parent, y_depth = dist[y]
        
        return x_depth == y_depth and x_parent != y_parent

    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        x_found, y_found = False, False
        x_parent, y_parent = None, None
        x_depth, y_depth = 0, 0
        
        q = [(0,root,None)]
        
        while q:
            d, node, par = q.pop()
            
            if node.val == x:
                x_found = True
                x_parent = par
                x_depth = d
            elif node.val == y:
                y_found = True
                y_parent = par
                y_depth = d
            
            if node.left:
                q.append((d+1,node.left,node))
            
            if node.right:
                q.append((d+1,node.right,node))
                
            if x_found and y_found:
                break
        
        return( (x_depth==y_depth) and (x_parent!=y_parent) and x_found and y_found)