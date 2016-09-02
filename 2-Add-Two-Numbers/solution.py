# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        output = head
        carry = 0
        while True:
            if l1 != None:
                carry = l1.val + carry
                l1 = l1.next
            if l2 != None:
                carry = l2.val + carry
                l2 = l2.next
            output.val = carry % 10
            carry = carry / 10
            if l1 != None or l2 != None or carry:
                output.next = ListNode(0)
                output = output.next
            else:
                break
        return head
            
            
        