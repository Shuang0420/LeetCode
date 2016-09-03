# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l2 is None:
            return l1 
        if l1 is None:
            return l2 
        if l1.val < l2.val:
            head = l1
            head.next = self.mergeTwoLists(l1.next,l2)
        else:
            head = l2
            head.next = self.mergeTwoLists(l1,l2.next)
        return head
  