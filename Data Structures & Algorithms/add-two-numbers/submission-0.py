class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, None)
        c = dummy
        carryover = 0
        while l1 != None or l2 != None or carryover != 0:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            total = v1 + v2 + carryover
            
            carryover = total // 10
            c.next = ListNode(total % 10, None)
            c = c.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        return dummy.next