# https://leetcode.com/problems/reverse-linked-list/
from typing import Optional
from linked_list import ListNode, convert_list_to_linkedlist


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev


sol = Solution()
print(sol.reverseList(convert_list_to_linkedlist([1, 2, 3, 4, 5])))
print(sol.reverseList(convert_list_to_linkedlist([1, 2])))
print(sol.reverseList(convert_list_to_linkedlist([])))
