class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        dummy = ListNode()
        current = dummy

        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            _sum = x + y + carry
            carry = _sum // 10

            current.next = ListNode(_sum % 10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry > 0:
            current.next = ListNode(carry)

        return dummy.next 