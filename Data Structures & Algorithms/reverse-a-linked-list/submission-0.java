/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode curr, prev, n;
        curr = head;
        prev = null;
        if (curr == null){
            return head;
        }
        n = curr.next;
        while (n != null){
            curr.next = prev;
            prev = curr;
            curr = n;
            n = curr.next;
        }
        curr.next = prev;
        head = curr;
        return head;
    }
            
}
