/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode(0); //create a dummy node
        dummy.next = head;
        ListNode first = dummy;
        ListNode second = dummy;
        // keep the gap=n between first and second
        for (int i=0; i<=n; i++) {
            first = first.next;
        }
        while (first != null) {
            first = first.next;
            second = second.next;
        } 
        //skip the Nth node from the end
        second.next = second.next.next;
        return dummy.next;
    }
}