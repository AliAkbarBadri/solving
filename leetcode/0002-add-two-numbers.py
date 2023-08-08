# https://leetcode.com/problems/add-two-numbers/
from typing import Optional
from linked_list import ListNode, convert_list_to_linkedlist


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not l1 and not l2:
            return ListNode()
        dummy = ListNode()
        head = dummy
        carry = 0
        while l1 and l2:
            val = l1.val + l2.val + carry
            carry = val // 10
            val = val % 10
            head.next = ListNode(val)
            l1 = l1.next
            l2 = l2.next
            head = head.next

        while l1:
            val = l1.val + carry
            carry = val // 10
            val = val % 10
            head.next = ListNode(val)
            l1 = l1.next
            head = head.next
        while l2:
            val = l2.val + carry
            carry = val // 10
            val = val % 10
            head.next = ListNode(val)
            l2 = l2.next
            head = head.next
        if carry:
            head.next = ListNode(carry)

        return dummy.next

    def addTwoNumbers2(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        head = dummy
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            head.next = ListNode(val)
            head = head.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next


sol = Solution()

assert (
    sol.addTwoNumbers(
        convert_list_to_linkedlist([9, 9, 1]),
        convert_list_to_linkedlist([1]),
    ).__str__()
    == convert_list_to_linkedlist([0, 0, 2]).__str__()
)


assert (
    sol.addTwoNumbers(
        convert_list_to_linkedlist([9, 9, 9, 9, 9, 9, 9]),
        convert_list_to_linkedlist([9, 9, 9, 9]),
    ).__str__()
    == convert_list_to_linkedlist([8, 9, 9, 9, 0, 0, 0, 1]).__str__()
)

assert (
    sol.addTwoNumbers(
        convert_list_to_linkedlist([0]), convert_list_to_linkedlist([0])
    ).__str__()
    == convert_list_to_linkedlist([0]).__str__()
)

assert (
    sol.addTwoNumbers(
        convert_list_to_linkedlist([2, 4, 3]), convert_list_to_linkedlist([5, 6, 4])
    ).__str__()
    == convert_list_to_linkedlist([7, 0, 8]).__str__()
)
