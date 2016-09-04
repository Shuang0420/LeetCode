# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self,head):
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        while head:
            while head.next and head.next.val == head.val:
                head.next = head.next.next
                if not head.next or head.next.val != head.val:
                    break
            else:
                cur.next = head
                cur = head
            head = head.next
        cur.next = None
        return dummy.next
        
