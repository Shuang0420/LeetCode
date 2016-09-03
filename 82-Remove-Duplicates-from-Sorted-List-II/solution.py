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
        cur = dummy
        while head:
            while head.next and head.val == head.next.val:
                head = head.next
                if not head.next or head.val != head.next.val:
                    break
            else:
                cur.next = head
                cur = head
            head = head.next
        cur.next = None
        return dummy.next
        
