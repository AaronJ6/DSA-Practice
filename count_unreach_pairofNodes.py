from collections import Counter

class dsu(object):
    def __init__(self,n):
        self.root = [i for i in range(n)]
        self.rank = [1]*n
    
    def find(self,x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self,x,y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root != y_root:
            if self.rank[x_root] > self.rank[y_root]:
                self.root[y_root] = x_root
            elif self.rank[y_root] > self.rank[x_root]:
                self.root[x_root] = y_root
            else:
                self.root[y_root] = x_root
                self.rank[x_root] += 1

def countPairs(n, edges):
    """
    :type n: int
    :type edges: List[List[int]]
    :rtype: int
    """
    obj = dsu(n)
    for u,v in edges:
        obj.union(u,v)
    C = Counter([obj.find(i) for i in range(n)])
    groupCounts = list(C.values())
    ans = 0
    firstGroupCount = groupCounts[0]
    for i in range(1, len(groupCounts)):
        ans += firstGroupCount * groupCounts[i]
        firstGroupCount += groupCounts[i]  
    return ans