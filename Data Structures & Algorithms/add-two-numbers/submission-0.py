class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node makes it easier to build the result list
        dummy = ListNode(0)
        current = dummy

        carry = 0

        # Continue while either list has digits left,
        # or there is still a carry to add
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry

            # Current digit goes into the result
            digit = total % 10

            # Carry goes to the next position
            carry = total // 10

            current.next = ListNode(digit)
            current = current.next

            # Move forward if the nodes exist
            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy.next