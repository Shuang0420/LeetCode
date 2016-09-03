# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        prev = dummy
        while head:
            while head.next and head.val == head.next.val:
                head.next = head.next.next
                if not head.next or head.val != head.next.val:
                    break
            else:
                prev.next = head
                prev = head
            head = head.next
        prev.next = None
        return dummy.next
        
