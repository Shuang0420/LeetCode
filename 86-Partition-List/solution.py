# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self,head,x):
        left,right = ListNode(0),ListNode(0)
        left_cur,right_cur=left,right
        while head:
            if head.val<x:
                left_cur.next,head=head,head.next
                left_cur=left_cur.next
            else:
                right_cur.next,head=head,head.next
                right_cur=right_cur.next
        left_cur.next=right.next
        right_cur.next=None
        return left.next
        
        