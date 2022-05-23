import heapq #!TREE DS where the parent node val is lesser than the children like a min heap


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists or len(lists)==0: #!NEETCODE + MY CODE
            return None
        
        while(len(lists)>1):
            merg = []
            
            for i in range(0,len(lists),2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1<len(lists) else None
                merg.append(self.merge_list(l1,l2))
            lists = merg
        return lists[0]
    
    def merge_list(self, l1, l2):
        dummy = ListNode()
        temp = dummy
        while l1 and l2:
            if l1.val<l2.val:
                dummy.next = l1
                l1 = l1.next
            else:
                dummy.next = l2
                l2 = l2.next
            dummy = dummy.next
        if l1:
            dummy.next = l1
        elif l2:
            dummy.next = l2
        return temp.next

"""     def mergeKLists(self, lists): #!FASTEST CODE IN LEETCODE
        
        # :type lists: List[ListNode]
        # :rtype: ListNode
        
        heap=[]
        for l in lists:
            if l is not None:
                heapq.heappush(heap, (l.val,l))
        head = point = ListNode(0)
        
        while heap:
            v, i = heapq.heappop(heap)
            point.next = i
            point = point.next
            if i.next is not None:
                heappush(heap, (i.next.val, i.next))

        return head.next """