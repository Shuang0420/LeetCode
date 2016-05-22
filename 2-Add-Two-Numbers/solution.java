/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int sum = l1.val + l2.val;
        int val = sum % 10;
        int carry = sum / 10;
        ListNode result = new ListNode(val);
        ListNode p = result;
        ListNode nextNode;
        l1 = l1.next;
        l2 = l2.next;
        while (l1 != null && l2 != null) {
            sum = l1.val + l2.val + carry;
            val = sum % 10;
            carry = sum / 10;
            nextNode = new ListNode(val);
            p.next = nextNode;
            p = nextNode;
            l1 = l1.next;
            l2 = l2.next;
        }
        ListNode n = (l1 != null ? l1 : l2);
        while (n != null) {
            sum = n.val + carry;
            val = sum % 10;
            carry = sum / 10;
            nextNode = new ListNode(val);
            p.next = nextNode;
            p = nextNode;
            n = n.next;
            
        }
        if (carry != 0) {
            p.next = new ListNode(carry);
        }
        return result;
    }
}