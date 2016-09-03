# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        left,right = ListNode(None),ListNode(None)
        left_cur,right_cur = left,right
        while head:
            if head.val < x:
                left_cur.next,head=head,head.next
                left_cur,left_cur.next = left_cur.next,None
            else:
                right_cur.next,head=head,head.next
                right_cur,right_cur.next = right_cur.next,None
        left_cur.next=right.next
        return left.next
        
        