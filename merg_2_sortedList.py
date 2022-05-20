# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2): #!NEETCODE simple implementation,
                                            #! didnt know how to make it on python properly
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        tail = dummy
        s1 = list1
        s2 = list2
        while(s1 != None and s2 != None):
            if s1.val <= s2.val:
                tail.next = s1
                s1 = s1.next
            else:
                tail.next = s2
                s2 = s2.next
            tail = tail.next
        if(s1 != None):
            tail.next = s1
        else:
            tail.next = s2
        op = dummy.next
        return(op)