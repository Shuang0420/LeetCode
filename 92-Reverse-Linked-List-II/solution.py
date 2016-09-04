# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m==n:
            return head
            
        # [1,m-1] nodes
        oup = ListNode(0)
        oup.next = head
        dummy = oup
        
        for i in range(m-1):
            dummy = dummy.next
            
        # reverse [m,n] nodes
        reverse = None
        cur = dummy.next
        for i in range(m,n+1):
            cur.next,reverse,cur = reverse,cur,cur.next
        
        # [n,end] nodes
        dummy.next.next = cur
        dummy.next = reverse
        
        return oup.next
                
        
        